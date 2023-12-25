from fastapi import FastAPI
from crud.ProductsCrud import Products
from crud.ProductsCrud import insDB, selDB
from crud.BuyProductsCrud import BuyProducts
from base.baseModels import Product, BuyProduct

app = FastAPI()

@app.get("/v1/products")
async def getProducts():
    data = Products.get()
    return {'data': data}

@app.post("/v1/products")
async def createProduct(product: Product):
    data = Products.post(product)
    return {'data': data, 'message': 'created with succesful.'}

@app.delete("/v1/products/{product_id}")
async def deleteProduct(product_id):
    data = Products.delete(product_id)
    return {'message': 'deleted with succesful.'}

@app.get("/v1/products/{product_id}") 
async def getOneProduct(product_id):
    data = Products.getById(product_id)
    return data

@app.get("/v1/buyProducts")
async def getBuyProducts():
    data = BuyProducts.get()
    return {'data': data}

@app.post("/v1/buyProducts")
async def insertBuyProduct(buyProduct: BuyProduct):
    data = BuyProducts.post(buyProduct)
    return data

@app.delete("/v1/buyProducts/{buy_id}")
async def deleteBuyProduct(buy_id):
    data = BuyProducts.delete(buy_id)
    return data
