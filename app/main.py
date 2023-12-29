from fastapi import FastAPI
from api import products, buyProducts, sellProducts
from querys.querys import getRecentBuys, allSells
from utils import tools as OSIOTools
from http import HTTPStatus
from wa_automate_socket_client import SocketClient

app = FastAPI()

app.include_router(products.router, prefix="/v1/products", tags=["products"])
app.include_router(buyProducts.router, prefix="/v1/buyProducts", tags=["buyProducts"])
app.include_router(sellProducts.router, prefix="/v1/sellProducts", tags=["sellProducts"])

@app.get("/v1/recentBuys")
async def recentBuys():
    data = getRecentBuys()
    if data:
        status = HTTPStatus.OK
    else:
        status = HTTPStatus.NOT_FOUND
    return OSIOTools.payloadSuccess(data, status)
 
@app.get("/v1/sells")
async def sells():
    data = allSells()
    return OSIOTools.payloadSuccess(data, statusCode=HTTPStatus.OK)

#@app.get("/sendMessage")
#async def sendMessageWPP():
#    NUMBER = '5527999221708@c.us'
#    client = SocketClient('http://localhost:8085/', 'secure_api_key')
#    client.onMessage(client.sendText(NUMBER, "entendi então ~ api"))
 #   client.disconnect()


