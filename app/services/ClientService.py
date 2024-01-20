from utils.tools import selDB, insDB, payloadError
from base.baseModels import Client
from http import HTTPStatus
from adapters.cep.api_cep import CepApi
import json

class Clients:
    def get():
        query = "select * from clients;"
        clients = selDB(query)
        return clients
    
    def getById(client_id):
        query = "select * from clients where client_id=%s"
        values = (client_id,)
        client = selDB(query, values)
        return {"data": client, "status": 200}

    def getClientAddress(cep):
        clientAddress = CepApi().getCep(cep)
        clientAddress = json.dumps(clientAddress)
        return clientAddress
    
    def getClientAddressById(client_id):
        client = Clients.getById(client_id)
        if client['status'] == 200:
            clientAddress = CepApi().getCep(client['data'][0]['cep'])
            return {"data": clientAddress, "status": 200}

    # Fazer um getbyid, puxar o CEP, dar um get na CEP API
    # Mas antes, mapear o retorno dos dados da CEP API!!


    def clientIsAdded(client: Client):
        query = "select * from clients where cel_number=%s"
        values = (client.cel_number,)
        client = selDB(query, values)
        return client
    
    def post(client: Client):
        if not Clients.clientIsAdded(client):
            client.address = Clients.getClientAddress(client.cep)
            query = "INSERT INTO clients (counterpart_name, document, cep, cel_number, address_json) VALUES (%s, %s, %s, %s, %s)"
            values = (client.counterpart_name, client.document, client.cep, client.cel_number, client.address)
            insDB(query, values)
            return client
        else:
            return payloadError(message="client already exists.", statusCode=HTTPStatus.CONFLICT)