from fastapi import FastAPI
from api import products, buyProducts

app = FastAPI()

app.include_router(products.router, prefix="/v1/products", tags=["products"])
app.include_router(buyProducts.router, prefix="/v1/buyProducts", tags=["buyProducts"])

