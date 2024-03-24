from utils.tools import selDB, insDB
from utils import tools
from osio.base.baseModels import SellProduct
import json

def basePayload(data, status):
    return {"data": data, "status": status}

class SellProducts:
    def get():
        query = "SELECT * FROM sell_products;"
        sells = selDB(query)
        return basePayload(sells, 200)
    
    def userSells(user_id):
        query = "select * from sell_products where user_id=%s;"
        values = (user_id, )
        userSells = selDB(query, values)
        return basePayload(userSells, 200)
    
    def userSellsProfit(user_id):
        query = "SELECT sell_products.id as sell_id, sell_products.price as price, products.product, clients.counterpart_name, clients.client_id, "
        query += "clients.cel_number, ((buy_products.price + buy_products.rate_product) / buy_products.quantity) as unit_price, (sell_products.price - ((buy_products.price + buy_products.rate_product) / buy_products.quantity)) as profit "
        query += "FROM sell_products INNER JOIN clients ON sell_products.client_id = clients.client_id INNER JOIN "
        query += "products ON products.id = sell_products.product_id INNER JOIN buy_products ON buy_products.id = sell_products.buy_id where clients.user_id = %s and sell_products.user_id = %s; "
        values = (user_id, user_id) 
        userSells = selDB(query, values)
        return basePayload(userSells, 200)
  
    def getById(sell_id):
        query = "SELECT * FROM sell_products where id=%s"
        values = (sell_id, )
        sell = selDB(query, values)
        if sell:
            return basePayload(sell, 200)
        else:
            return {"error": {"message": "Sell not found"}, "status": 404}
    
    def post(sellProduct: SellProduct):
        query = "insert into sell_products (product_id, buy_id, client_id, price, sell_date) values (%s, %s, %s, %s, %s)"
        values = (sellProduct.product_id, sellProduct.buy_id, sellProduct.client_id, sellProduct.price, sellProduct.sell_date)
        sellId = insDB(query, values)
        query = "update products set quantity = quantity - 1 where id="+str(sellProduct.product_id)+""
        insDB(query, values=None)
        sellCreated = SellProducts.getById(sellId)
        if "data" in sellCreated:
            return basePayload(sellCreated['data'], 201)
        else:
            {"error": {"message": "product not created"}, "status": 500}
    
    def put(sell_product): pass

    def delete(sell_id):
        dataToDelete = SellProducts.getById(sell_id)
        if not "error" in dataToDelete:
            query = "delete from sell_products where id=%s"
            values = (sell_id,)
            insDB(query, values)
            return {"message": "delete with successful."}
        else:
            return tools.payloadError("Sell not found", 404)

#insert into sell_products (product_id, buy_id, price, sell_date) values (7, 12, 155.0, NOW())