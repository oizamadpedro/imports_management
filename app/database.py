import mysql.connector
import os
import dotenv

dotenv.load_dotenv('.././imports_m.env')

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

config = {
  'user': DB_USER,
  'password': DB_PASSWORD,
  'host': DB_HOST,
  'database': DB_NAME
}

def selectAllProducts():
  db = mysql.connector.connect(**config)
  cursor = db.cursor(dictionary=True)
  query = ("SELECT * FROM products;")
  result = cursor.execute(query)
  rows = cursor.fetchall()
  db.close()
  return rows

def insertProduct(product):
    db = mysql.connector.connect(**config)
    cursor = db.cursor(dictionary=True)
    query = "INSERT INTO products (product, price, buy_date, rate_product, sell_date, quantity) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (product.product, product.price, product.buy_date, product.rate_product, product.sell_date, product.quantity)
    cursor.execute(query, values)
    db.commit()
    cursor.close()
    db.close()
    
    return product


