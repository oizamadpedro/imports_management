from utils.tools import selDB, insDB
from base.baseModels import Product
from utils import tools

class Products:
  def __init__(self, query, values=None):
    self.query = query
    self.values = values

  def get():
    query = "SELECT * FROM products;"
    products = selDB(query)
    return tools.payloadSuccess(products, 200)

  def getById(product_id):
    query = "SELECT * FROM products where id=%s"
    values = (product_id, )
    products = selDB(query, values)
    if products:
      return tools.payloadSuccess(products, 200)
    else:
      return tools.payloadError("Product not found.", 404)

  def post(product: Product):
    query = "INSERT INTO products (product, quantity, description) VALUES (%s, %s, %s)"
    values = (product.product, product.quantity, product.description)
    insDB(query, values)
    return tools.payloadSuccess(product, 201)

  def put(product): pass

  def delete(product_id):
    productToDelete = Products.getById(product_id)
    if not "error" in productToDelete:
      query = "delete from products where id=%s"
      values = (product_id,)
      insDB(query, values)
      return {'message': 'deleted with successful.'}
    else:
      return tools.payloadError("Product not found.", 404)