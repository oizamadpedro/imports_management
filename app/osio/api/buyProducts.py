from fastapi import APIRouter, Response
from services.BuyProductService import BuyProducts
from base.baseModels import BuyProduct
from utils import tools
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from adapters.auth.client import AuthClient

security = HTTPBearer()
router = APIRouter()

@router.get("/")
async def getBuyProducts(credentials: HTTPAuthorizationCredentials = Security(security)):
    if credentials:
        token = credentials.credentials
        print(token)
        data = AuthClient.userDetails(token)
        print(data)
        if "error" in data:
            return data
        else:
            print(data)
            user_id = data['data']['id']  # Assumindo que o ID do usuário está presente no token JWT
            data = BuyProducts.userBuys(user_id)
            return data
    else:
        return Response(status_code=401, detail="Invalid authorization credentials")

    
    return data

@router.get("/{buy_id}")
async def getOneProduct(buy_id):
    data = BuyProducts.getById(buy_id)
    return data

@router.post("/")
async def insertBuyProduct(buyProduct: BuyProduct):
    data = BuyProducts.post(buyProduct)
    return data

@router.delete("/{buy_id}")
async def deleteBuyProduct(buy_id):
    data = BuyProducts.delete(buy_id)
    return data

