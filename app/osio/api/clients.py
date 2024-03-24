from fastapi import APIRouter
from osio.services.ClientService import Clients
from osio.base.baseModels import Client
from fastapi.responses import Response
import json
from utils.tools import getUserData
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
 
security = HTTPBearer()
router = APIRouter()

def payloadReturn(data):
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data.get("status", None))

@router.get("/")
def clients(credentials: HTTPAuthorizationCredentials = Security(security)):
    user_data = getUserData(credentials)
    user_id = user_data.get("id", None)
    if user_id:
        data = Clients.userClients(user_id)
        return payloadReturn(data)
    return payloadReturn(user_data)

@router.get("/{client_id}")
def getClientById(client_id):
    data = Clients.getById(client_id)
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data['status'])

@router.get("/sells/{client_id}") # pega todas as vendas desse cliente
def clientSells(client_id):
    data = Clients.getClientSells(client_id)
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data['status'])

@router.get("/address/{client_id}")
def clientAddress(client_id):
    data = Clients.getClientAddressById(client_id)
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data['status'])

@router.post("/")
def insert_client(client: Client):
    client = Clients.post(client)
    return {'data': client}
