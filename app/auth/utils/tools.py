import mysql.connector
import os
import dotenv
import json
from http import HTTPStatus
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Dict

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
  last_inserted_id = cursor.lastrowid
  cursor.close()
  db.close()
  return last_inserted_id

def selDB(query, values=None):
  db = mysql.connector.connect(**config)
  cursor = db.cursor(dictionary=True)
  result = cursor.execute(query, values)
  rows = cursor.fetchall()
  db.close()
  return rows

def payloadSuccess(data, status):
  data = jsonable_encoder(data)
  json_payload =  {
    "data": data,
    "status": status
  }
  return JSONResponse(status_code=status, content=json_payload)

def payloadError(message, status):
  json_payload = {"error": { "message": message }, "status": status}
  return JSONResponse(status_code=status, content=json_payload)



