from fastapi import FastAPI
from pydantic import BaseModel
from database import selectAllProducts, insertProduct, delete, selectOneProduct

class Product(BaseModel):
    product: str
    price: float
    buy_date: str
    rate_product: float | None = None
    sell_date: str | None = None
    quantity: int

app = FastAPI()

@app.get("/v1/products")
async def getProducts():
    data = selectAllProducts()
    return {'data': data}

@app.post("/v1/products")
async def createProduct(product: Product):
    data = insertProduct(product)
    return {'data': data, 'message': 'created with succesful.'}

@app.delete("/v1/products/{product_id}")
async def deleteProduct(product_id):
    data = delete(product_id)
    return {'message': 'deleted with succesful.'}

@app.get("/v1/products/{product_id}")
async def getOneProduct(product_id):
    data = selectOneProduct(product_id)
    return {'data': data}