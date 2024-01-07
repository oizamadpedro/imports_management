from utils.tools import selDB, insDB
from base.baseModels import Client

class Clients:
    def get():
        query = "select * from clients;"
        clients = selDB(query)
        return clients
    
    def post(client: Client):
        query = "INSERT INTO clients (counterpart_name, document, cep, cel_number) VALUES (%s, %s, %s, %s)"
        values = (client.counterpart_name, client.document, client.cep, client.cel_number)
        insDB(query, values)
        return client