from fastapi import APIRouter, Depends
from dependencies import pegar_sessao
from models import Usuario
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth",tags=["Auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa é a rota padrão de autenticação do nosso sistema. Todas as rotas dos pedidos precisam de autenticação
    """
  
    return {"mensagem":"Você acessou a rota padrão de autenticação",
            "autenticado":False}

@auth_router.post("/criar_conta")
async def criar_conta(email:str,senha:str,nome:str, session=Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).all()
    if usuario:
        # Já existe um usuario com esse email
        return {"mensagem":"Já existe um usuario com esse email"}
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome,email,senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem":"Usuario cadastrado com sucesso"}



