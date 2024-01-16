from fastapi import APIRouter
import json
from fastapi.responses import JSONResponse
from services.ProductService import Products
from base.baseModels import Product

router = APIRouter()

@router.get("/")
async def getProducts():
    data = Products.get()
    return data

@router.post("/")
async def createProduct(product: Product):
    data = Products.post(product)
    return JSONResponse(status_code=data['status'], content=json.dumps(data))

@router.delete("/{product_id}")
async def deleteProduct(product_id):
    data = Products.delete(product_id)
    return JSONResponse(status_code=data['status'], content=json.dumps(data))

@router.get("/{product_id}")
async def getOneProduct(product_id):
    data = Products.getById(product_id)
    return JSONResponse(status_code=data['status'], content=json.dumps(data))