from utils.tools import selDB, insDB
from base.baseModels import BuyProduct

class BuyProducts:
    def __init__(self, query, values=None):
        self.query = query
        self.values = values

    def get():
        query = "SELECT * FROM buy_products;"
        products = selDB(query)
        return products
  
    def getById(buy_id):
        query = "SELECT * FROM buy_products where id=%s"
        values = (buy_id, )
        products = selDB(query, values)
        return products
    
    def post(buyProduct: BuyProduct):
        query = "insert into buy_products (product_id, price, rate_product, shop, buy_date, quantity) values (%s, %s, %s, %s, %s, %s)"
        values = (buyProduct.product_id, buyProduct.price, buyProduct.rate_product, buyProduct.shop, buyProduct.buy_date, buyProduct.quantity)
        aux = insDB(query, values)
        return aux
  
    def put(product): pass

    def delete(buy_id):
        query = "delete from buy_products where id=%s"
        values = (buy_id,)
        insDB(query, values)
        return True