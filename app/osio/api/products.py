from fastapi import APIRouter
import json
from fastapi.responses import Response
from services.ProductService import Products
from base.baseModels import Product

router = APIRouter()

def payloadReturn(data):
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data['status'])

@router.get("/")
async def getProducts():
    data = Products.get()
    return payloadReturn(data)

@router.post("/")
async def createProduct(product: Product):
    data = Products.post(product)
    return payloadReturn(data)

@router.delete("/{product_id}")
async def deleteProduct(product_id):
    data = Products.delete(product_id)
    return payloadReturn(data)

@router.get("/{product_id}")
async def getOneProduct(product_id):
    data = Products.getById(product_id)
    return payloadReturn(data)