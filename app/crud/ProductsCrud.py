from utils.tools import selDB, insDB

class Products:
  def __init__(self, query, values=None):
    self.query = query
    self.values = values

  def get():
    query = "SELECT * FROM products;"
    products = selDB(query)
    return products
  
  def getById(product_id):
    query = "SELECT * FROM products where id=%s"
    values = (product_id, )
    products = selDB(query, values)
    return products

  def post(product):
    query = "INSERT INTO products (product, price, buy_date, rate_product, sell_date, quantity) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (product.product, product.price, product.buy_date, product.rate_product, product.sell_date, product.quantity)
    insDB(query, values)
    return product
  
  def put(product): pass

  def delete(product_id):
    query = "delete from products where id=%s"
    values = (product_id,)
    insDB(query, values)
    return True
