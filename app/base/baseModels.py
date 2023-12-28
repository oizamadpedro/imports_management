from pydantic import BaseModel

#base for buyproducts
class BuyProduct(BaseModel):
    product_id: int
    price: float
    rate_product: float = None
    shop: str
    buy_date: str
    quantity: int
    order_id: str
    
class Product(BaseModel):
    product: str
    description: str
    quantity: int