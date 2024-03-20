from fastapi import FastAPI
from api import products, buyProducts, sellProducts, clients, users
from querys.querys import getRecentBuys, allSells, sellProfit
from utils import tools as OSIOTools
from http import HTTPStatus
from wa_automate_socket_client import SocketClient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",  # Adicione os domínios permitidos aqui
    "https://seu-outro-dominio.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # ou especifique os métodos permitidos
    allow_headers=["*"],  # ou especifique os cabeçalhos permitidos
)

app.include_router(products.router, prefix="/osio/v1/products", tags=["products"])
app.include_router(buyProducts.router, prefix="/osio/v1/buyProducts", tags=["buyProducts"])
app.include_router(sellProducts.router, prefix="/osio/v1/sellProducts", tags=["sellProducts"])
app.include_router(clients.router, prefix="/osio/v1/clients", tags=["clients"])
app.include_router(users.router, prefix="/osio/v1/users", tags=["users"])

@app.get("/osio/v1/buys")
async def recentBuys():
    data = getRecentBuys()
    return OSIOTools.payloadSuccess(data, 200)
 
@app.get("/osio/v1/sells")
async def sells():
    data = allSells()
    return OSIOTools.payloadSuccess(data, 200)

@app.get("/osio/v1/sellProfit")
async def allSellProfit():
    data = sellProfit()
    return OSIOTools.payloadSuccess(data, 200)