from pydantic import BaseModel

class Product(BaseModel):
    product: str
    description: str
    quantity: int