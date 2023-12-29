from utils.tools import selDB, insDB
from base.baseModels import SellProduct

class SellProducts:
    def get():
        query = "SELECT * FROM sell_products;"
        sells = selDB(query)
        return sells
  
    def getById(sell_id):
        query = "SELECT * FROM sell_products where id=%s"
        values = (sell_id, )
        sell = selDB(query, values)
        return sell
    
    def post(sellProduct: SellProduct):
        query = "insert into sell_products (product_id, buy_id, price, sell_date) values (%s, %s, %s, %s)"
        values = (sellProduct.product_id, sellProduct.buy_id, sellProduct.price, sellProduct.sell_date)
        aux = insDB(query, values)
        return aux
    
    def put(sell_product): pass

    def delete(sell_id):
        query = "delete from sell_products where id=%s"
        values = (sell_id,)
        insDB(query, values)
        return True




#insert into sell_products (product_id, buy_id, price, sell_date) values (7, 12, 155.0, NOW())