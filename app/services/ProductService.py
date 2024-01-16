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
    return {"data": products, "status": 200}

  def getById(product_id):
    query = "SELECT * FROM products where id=%s"
    values = (product_id, )
    products = selDB(query, values)
    if products:
      return {"data": products, "status": 200}
    else:
      return {"error": {"message": "product not found"}, "status": 404}

  def post(product: Product):
    query = "INSERT INTO products (product, quantity, description) VALUES (%s, %s, %s)"
    values = (product.product, product.quantity, product.description)
    productId = insDB(query, values)
    productCreated = Products.getById(productId)
    if "data" in productCreated:
      return {"data": productCreated['data'], "status": 201}
    else:
      return {"error": {"message": "product not created"}, "status": 500}

  def put(product): pass

  def delete(product_id):
    productToDelete = Products.getById(product_id)
    if "error" not in productToDelete:
      query = "delete from products where id=%s"
      values = (product_id,)
      insDB(query, values)
      return {'message': 'deleted with successful.', "status": 200}
    else:
      return {"error": {"message": "product not found"}, "status": 404}