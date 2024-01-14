from utils.tools import selDB, insDB, payloadError
from base.baseModels import Client
from http import HTTPStatus

class Clients:
    def get():
        query = "select * from clients;"
        clients = selDB(query)
        return clients
    
    def clientIsAdded(client: Client):
        query = "select * from clients where cel_number=%s"
        values = (client.cel_number,)
        client = selDB(query, values)
        return client
    
    def post(client: Client):
        if not Clients.clientIsAdded(client):
            query = "INSERT INTO clients (counterpart_name, document, cep, cel_number) VALUES (%s, %s, %s, %s)"
            values = (client.counterpart_name, client.document, client.cep, client.cel_number)
            insDB(query, values)
            return client
        else:
            return payloadError(message="client already exists.", statusCode=HTTPStatus.CONFLICT)