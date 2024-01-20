from fastapi import APIRouter
from services.ClientService import Clients
from base.baseModels import Client
from fastapi.responses import Response
import json

router = APIRouter()

@router.get("/")
def clients():
    clients = Clients.get()
    return {'data': clients}

@router.get("/{client_id}")
def getClientById(client_id):
    data = Clients.getById(client_id)
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data['status'])

@router.get("/address/{client_id}")
def clientAddress(client_id):
    data = Clients.getClientAddressById(client_id)
    return Response(content=json.dumps(data),  media_type="application/json", status_code=data['status'])

@router.post("/")
def insert_client(client: Client):
    client = Clients.post(client)
    return {'data': client}
