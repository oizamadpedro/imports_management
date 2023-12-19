from fastapi import FastAPI
from pydantic import BaseModel
from database import selectAllProducts, insertProduct

class Product(BaseModel):
    product: str
    price: float
    buy_date: str
    rate_product: float | None = None
    sell_date: str | None = None
    quantity: int

app = FastAPI()

@app.get("/v1/getProducts")
async def getProducts():
    data = selectAllProducts()
    return {'data': data}

@app.post("/v1/createProduct")
async def createProduct(product: Product):
    data = insertProduct(product)
    return {'data': data, 'message': 'created with succesful.'}

