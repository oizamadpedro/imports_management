from utils.tools import selDB, insDB
from osio.base.baseModels import Product

class Products:
  def __init__(self, query, values=None):
    self.query = query
    self.values = values

  def get():
    query = "SELECT * FROM products;"
    products = selDB(query)
    return {"data": products, "status": 200} 
  
  def userProducts(user_id):
    query = "select * from products where user_id=%s;"
    values = (user_id, )
    products = selDB(query, values)
    return {"data": products, "status": 200}
  
  def userCreateProduct(product: Product, user_id):
    query = "INSERT INTO PRODUCTS(product, quantity, description, user_id) VALUES (%s, %s, %s, %s)"
    values = (product.product, product.quantity, product.description, user_id)
    productId = insDB(query, values)
    return {"data": f"created product {productId}", "status": 201}
      
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

  def delete(product_id, user_id):
    productToDelete = Products.getById(product_id)
    if "error" not in productToDelete:
      query = "delete from products where id=%s and user_id = %s"
      values = (product_id, user_id)
      insDB(query, values)
      return {'message': 'deleted with successful.', "status": 200}
    else:
      return {"error": {"message": "product not found"}, "status": 404}