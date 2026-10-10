from fastapi import APIRouter, Depends, HTTPException
from dependencies import pegar_sessao
from models import Usuario
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter(prefix="/auth",tags=["Auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema. Todas as rotas dos pedidos precisam de autenticação
    """
  
    return {"mensagem":"Você acessou a rota padrão de autenticação",
            "autenticado":False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema:UsuarioSchema, session:Session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).all()
    if usuario:
        # Já existe um usuario com esse email
        raise HTTPException(status_code=400, detail="Email do usuário já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome,usuario_schema.email,senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem":f"Usuario cadastrado com sucesso {usuario_schema.email}"}



