from fastapi import APIRouter, Response, Security
from osio.services.SellProductService import SellProducts
from osio.base.baseModels import SellProduct
from utils.tools import getUserData
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import json

security = HTTPBearer()
router = APIRouter()

def payloadReturn(data):
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data.get("status", None))

@router.get("/")
async def sellProducts(credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = SellProducts.userSellsProfit(user_id)
        return data
    return user_data 

@router.get("/{sell_id}")
async def getASell(sell_id):
    data = SellProducts.getById(sell_id)
    return data

@router.post("/")
async def insertSell(sellProduct: SellProduct):
    data = SellProducts.post(sellProduct)
    return data

@router.delete("/{sell_id}")
async def deleteSell(sell_id):
    data = SellProducts.delete(sell_id)
    return data

