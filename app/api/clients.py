from fastapi import APIRouter
from services.ClientService import Clients
from base.baseModels import Client

router = APIRouter()

@router.get("/")
def clients():
    clients = Clients.get()
    return {'data': clients}