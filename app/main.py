from fastapi import FastAPI
from crud.ProductsCrud import Products
from crud.ProductsCrud import insDB, selDB
from base.baseProduct import Product
from base.baseBuyProduct import BuyProduct

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
    return {'data': data}

@app.post("/v1/buyProduct")
async def insertBuyProduct(buyProduct: BuyProduct):
    query = "insert into buy_products (product_id, price, rate_product, shop, buy_date, quantity) values (%s, %s, %s, %s, %s, %s)"
    values = (buyProduct.product_id, buyProduct.price, buyProduct.rate_product, buyProduct.shop, buyProduct.buy_date, buyProduct.quantity)
    # to date, NOW() is the actual datetime
    aux = insDB(query, values)
    return aux

@app.get("/v1/buyProducts")
async def getBuyProducts():
    query = "select * from buy_products"
    aux = selDB(query)
    return {'data': aux}