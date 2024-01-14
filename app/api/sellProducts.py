from fastapi import APIRouter
from services.SellProductService import SellProducts
from base.baseModels import SellProduct

router = APIRouter()

@router.get("/")
async def sellProducts():
    data = SellProducts.get()
    return data

@router.get("/{sell_id}")
async def getASell(sell_id):
    data = SellProducts.getById(sell_id)
    return data

@router.post("/")
async def insertSell(sellProduct: SellProduct):
    data = SellProducts.post(sellProduct)
    return data

@router.delete("/{sell_id}")
async def deleteSell(sell_id):
    data = SellProducts.delete(sell_id)
    return data
