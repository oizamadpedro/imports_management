from fastapi import APIRouter
import json
from fastapi.responses import Response
from osio.services.ProductService import Products
from osio.base.baseModels import Product
from auth.routes.auth import decodeToken
from utils.tools import getUserData
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

security = HTTPBearer()
router = APIRouter()

def payloadReturn(data):
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data.get("status", None))

@router.get("/")
async def getProducts(credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = Products.userProducts(user_id)
        return payloadReturn(data)
    return payloadReturn(user_data)

@router.post("/")
async def createProduct(product: Product, credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = Products.userCreateProduct(product, user_id)
        return payloadReturn(data)
    return payloadReturn(user_data)

@router.delete("/{product_id}")
async def deleteProduct(product_id, credentials: HTTPAuthorizationCredentials = Security(security)):
    data = Products.delete(product_id)
    return payloadReturn(data)

@router.get("/{product_id}")
async def getOneProduct(product_id, credentials: HTTPAuthorizationCredentials = Security(security)):
    data = Products.getById(product_id)
    return payloadReturn(data)