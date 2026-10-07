from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos",tags=["order"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrao de pedidos do sistema
    """
    return {"mensagem":"Você acessou a rota de pedidos"}