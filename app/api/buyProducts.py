from fastapi import APIRouter
from services.BuyProductService import BuyProducts
from base.baseModels import BuyProduct

router = APIRouter()

@router.get("/")
async def getBuyProducts():
    data = BuyProducts.get()
    return {'data': data}

@router.get("/{buy_id}")
async def getOneProduct(buy_id):
    data = BuyProducts.getById(buy_id)
    return {'data': data}

@router.post("/")
async def insertBuyProduct(buyProduct: BuyProduct):
    data = BuyProducts.post(buyProduct)
    return {'data': data, 'message': 'created with succesful.'}

@router.delete("/{buy_id}")
async def deleteBuyProduct(buy_id):
    data = BuyProducts.delete(buy_id)
    return data

