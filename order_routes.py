from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from schemas import PedidoSchema
from models import Pedido

order_router = APIRouter(prefix="/pedidos",tags=["order"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrao de pedidos do sistema
    """
    return {"mensagem":"Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema:PedidoSchema,session:Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"mensagem":f"pedido criado com sucesso, ID do pedido: {novo_pedido.id}"}