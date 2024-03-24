from fastapi import FastAPI
from osio.api import products, buyProducts, sellProducts, clients, users
from osio.querys.querys import getRecentBuys, allSells, sellProfit
from utils import tools as OSIOTools
from http import HTTPStatus
from wa_automate_socket_client import SocketClient
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import auth
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
 
security = HTTPBearer()
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

app.include_router(products.router, prefix="/v1/products", tags=["products"])
app.include_router(buyProducts.router, prefix="/v1/buyProducts", tags=["buyProducts"])
app.include_router(sellProducts.router, prefix="/v1/sellProducts", tags=["sellProducts"])
app.include_router(clients.router, prefix="/v1/clients", tags=["clients"])
app.include_router(users.router, prefix="/v1/users", tags=["users"])
app.include_router(auth.router, prefix="/auth/v1", tags=["auth"])

@app.get("/v1/buys")
async def recentBuys(credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = OSIOTools.getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = getRecentBuys(user_id)
        return OSIOTools.payloadSuccess(data, 200)
    return OSIOTools.payloadSuccess(user_data, 200)

@app.get("/v1/sells")
async def sells(credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = OSIOTools.getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = allSells(user_id)
        return OSIOTools.payloadSuccess(data, 200)
    return OSIOTools.payloadSuccess(user_data, 200)
