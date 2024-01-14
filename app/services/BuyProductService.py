from utils.tools import selDB, insDB
from utils import tools
from base.baseModels import BuyProduct

class BuyProducts:
    def __init__(self, query, values=None):
        self.query = query
        self.values = values

    def get():
        query = "SELECT * FROM buy_products;"
        products = selDB(query)
        return tools.payloadSuccess(products, 200)
  
    def getById(buy_id):
        query = "SELECT * FROM buy_products where id=%s"
        values = (buy_id, )
        product = selDB(query, values)
        if product:
            return tools.payloadSuccess(product, 200)
        else:
            return tools.payloadError("Product not found", 404)
    
    def post(buyProduct: BuyProduct):
        query = "insert into buy_products (product_id, price, rate_product, shop, quantity, order_id) values (%s, %s, %s, %s, %s, %s)"
        values = (buyProduct.product_id, buyProduct.price, buyProduct.rate_product, buyProduct.shop, buyProduct.quantity, buyProduct.order_id)
        aux = insDB(query, values)
        query = "update products set quantity = quantity + "+str(buyProduct.quantity)+" where id="+str(buyProduct.product_id)+""
        aux = insDB(query, values=None)
        return tools.payloadSuccess(buyProduct, 201)
  
    def put(product): pass

    def delete(buy_id):
        if not "error" in BuyProducts.getById(buy_id):
            query = "delete from buy_products where id=%s"
            values = (buy_id,)
            insDB(query, values)
            return {"message": "delete with successful"}
        else:
            return tools.payloadError("Buy not found", 404)
        return 