from utils.tools import selDB, insDB
from osio.base.baseModels import BuyProduct

class BuyProducts:
    def __init__(self, query, values=None):
        self.query = query
        self.values = values

    def get(): 
        query = "SELECT * FROM buy_products;"
        products = selDB(query)
        return {"data": products, "status": 200}
    
    def userBuys(user_id):
        query = "select * from buy_products where user_id=%s;"
        values = (user_id,)
        buys = selDB(query, values)
        return {"data": buys, "status": 200}
  
    def getById(buy_id, user_id):
        query = "SELECT * FROM buy_products where id=%s and user_id=%s;"
        values = (buy_id, user_id)
        product = selDB(query, values)
        if product:
            return {"data": product, "status": 200}
        else:
            return {"error": {"message": "buy product not found."}, "status": 404}

    def userCreateBuy(buyProduct: BuyProduct, user_id):
        query = "insert into buy_products (product_id, price, rate_product, shop, quantity, order_id, user_id) values (%s, %s, %s, %s, %s, %s, %s)"
        values = (buyProduct.product_id, buyProduct.price, buyProduct.rate_product, buyProduct.shop, buyProduct.quantity, buyProduct.order_id, user_id)
        buyId = insDB(query, values)
        query = f"update products set quantity = quantity + {buyProduct.quantity} where id={buyProduct.product_id}"
        insDB(query, values=None)
        buyCreated = BuyProducts.getById(buyId)
        if "data" in buyCreated:
            return {"data": buyCreated['data'], "status": 201}
        else:
            return {"error": {"message": "product not created"}, "status": 500}
  
    def put(product): pass

    def delete(buy_id, user_id):
        if not "error" in BuyProducts.getById(buy_id):
            query = "delete from buy_products where id=%s and user_id=%s;"
            values = (buy_id, user_id)
            insDB(query, values)
            return {"message": "delete with successful", "status": 200}
        else:
            return {"error": {"message": "buy not found"}, "status": 404}