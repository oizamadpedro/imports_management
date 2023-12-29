from fastapi import FastAPI
from api import products, buyProducts, sellProducts
from querys.querys import getRecentBuys
from utils import tools as OSIOTools
from http import HTTPStatus

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
 