from fastapi import APIRouter, Response
from osio.services.BuyProductService import BuyProducts
from osio.base.baseModels import BuyProduct
from utils.tools import getUserData
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import json

security = HTTPBearer()
router = APIRouter()
 
def payloadReturn(data):
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data.get("status", None))
 
@router.get("/")
async def getBuyProducts(credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = BuyProducts.userBuys(user_id)
        return data
    return user_data

@router.get("/{buy_id}")
async def getOneProduct(buy_id, credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = BuyProducts.getById(buy_id, user_id)
        return data
    return user_data

@router.post("/")
async def createProduct(buyProduct: BuyProduct, credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = BuyProducts.userCreateBuy(buyProduct, user_id)
        return payloadReturn(data)
    return payloadReturn(user_data)

@router.delete("/{buy_id}")
async def deleteBuyProduct(buy_id, credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = BuyProducts.delete(buy_id, user_id)
        return payloadReturn(data)
    return payloadReturn(user_data)

