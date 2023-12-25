from pydantic import BaseModel

#base for buyproducts
class BuyProduct(BaseModel):
    product_id: int
    price: float
    rate_product: float
    shop: str
    buy_date: str
    quantity: int
    
class Product(BaseModel):
    product: str
    description: str
    quantity: int