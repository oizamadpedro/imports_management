from utils.tools import selDB, insDB
from base.baseModels import Client

class Clients:
    def get():
        query = "select * from clients;"
        clients = selDB(query)
        return clients