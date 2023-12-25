from utils.tools import selDB, insDB
from base.baseModels import Product

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

  def post(product: Product):
    query = "INSERT INTO products (product, quantity, description) VALUES (%s, %s, %s)"
    values = (product.product, product.quantity, product.description)
    insDB(query, values)
    return product

  def put(product): pass

  def delete(product_id):
    query = "delete from products where id=%s"
    values = (product_id,)
    insDB(query, values)
    return {'message': 'deleted with successful.'}