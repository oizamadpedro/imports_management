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

def insDB(query, values): 
  db = mysql.connector.connect(**config)
  cursor = db.cursor(dictionary=True)
  cursor.execute(query, values)
  db.commit()
  cursor.close()
  db.close()
  return {'message': 'created with successful.'}

def selDB(query, values=None):
  db = mysql.connector.connect(**config)
  cursor = db.cursor(dictionary=True)
  result = cursor.execute(query, values)
  rows = cursor.fetchall()
  db.close()
  return rows

def payloadSuccess(data, statusCode):
  return {
    "data": data,
    "statusCode": statusCode
  }

def payloadError(message, statusCode):
  return {
    "error": {
      "message": message,
      "statusCode": statusCode
    }
  }