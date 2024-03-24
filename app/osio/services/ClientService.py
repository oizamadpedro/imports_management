from utils.tools import selDB, insDB, payloadError
from osio.base.baseModels import Client
from http import HTTPStatus
from osio.adapters.cep.api_cep import CepApi
import json

class Clients:
    def get():
        query = "select * from clients;"
        clients = selDB(query) 
        return clients 
    
    def userClients(user_id):
        query = "select * from clients where user_id=%s;"
        values = (user_id, )
        userClients = selDB(query, values)
        return {"data": userClients, "status": 200}

    def getById(client_id, user_id):
        query = "select * from clients where client_id=%s and user_id=%s;"
        values = (client_id, user_id)
        client = selDB(query, values)
        return {"data": client, "status": 200}

    def getClientSells(client_id, user_id):
        query = "SELECT sell_products.id as sell_id, sell_products.price as price, products.product, clients.counterpart_name, clients.client_id, "
        query += "clients.cel_number, ((buy_products.price + buy_products.rate_product) / buy_products.quantity) as unit_price, (sell_products.price - ((buy_products.price + buy_products.rate_product) / buy_products.quantity)) as profit "
        query += "FROM sell_products INNER JOIN clients ON sell_products.client_id = clients.client_id INNER JOIN "
        query += "products ON products.id = sell_products.product_id INNER JOIN buy_products ON buy_products.id = sell_products.buy_id where clients.client_id=%s and clients.user_id=%s and sell_products.user_id=%s and buy_products.user_id=%s;"
        values = (client_id, user_id, user_id, user_id)
        allSellsToClient = selDB(query, values)
        return {"data": allSellsToClient, "status": 200} # falta fazer verificação se esse cliente existe e se ele ja comprou com nois

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

    def clientIsAdded(client: Client, user_id):
        query = "select * from clients where cel_number=%s and user_id=%s"
        values = (client.cel_number, user_id)
        client = selDB(query, values)
        return client
    
    def post(client: Client, user_id):
        print(f"client ---> {client}")
        if not Clients.clientIsAdded(client, user_id):
            client.address = Clients.getClientAddress(client.cep)
            query = "INSERT INTO clients (counterpart_name, document, cep, cel_number, address_json, user_id) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (client.counterpart_name, client.document, client.cep, client.cel_number, client.address, user_id)
            insDB(query, values)
            return {"data": [], "message": "created with successful", "status": 201}
        else:
            return {"data": [], "message": "client already exists", "status": 400}