from fastapi import APIRouter, Depends, HTTPException
from dependencies import pegar_sessao
from models import Usuario
from main import bcrypt_context, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from schemas import LoginSchema, UsuarioSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import date, datetime, timedelta, timezone

auth_router = APIRouter(prefix="/auth",tags=["Auth"])

def criar_token(id_usuario):
    data_expericao = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dic_info = {"sub":id_usuario,"exp":data_expericao}
    
    jwt_codificado = jwt.encode(dic_info,SECRET_KEY,ALGORITHM)
    return jwt_codificado

def autenticar_usuario(email:str, senha:str, session:Session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    usuario_senha = bcrypt_context.verify(senha,usuario.senha)

    if not usuario:
        return False
    elif not usuario_senha:
        return False
    return usuario


@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema. Todas as rotas dos pedidos precisam de autenticação
    """
  
    return {"mensagem":"Você acessou a rota padrão de autenticação",
            "autenticado":False}


@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema:UsuarioSchema, session:Session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        # Já existe um usuario com esse email
        raise HTTPException(status_code=400, detail="Email do usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome,usuario_schema.email,senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem":f"Usuario cadastrado com sucesso {usuario_schema.email}"}

# login -> email e senha -> token JWT (Json Web Token) adffdafdff
@auth_router.post("/login")
async def login(login_schema:LoginSchema, session:Session=Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email,login_schema.senha,session)
    if not usuario:
        raise HTTPException(status_code=400,detail="Usuário não encontrado")
    else:
        acess_token = criar_token(usuario.id)
        return {
            "access_token": acess_token,
            "token_type": "Bearer"
        }
