# coding: utf-8
from pymongo import MongoClient

# classe intermediária entre o banco de dados e os scripts
class MongoDB:

  # variável contendo o banco
  db = MongoClient().price_watch

  # método de inserção simples, apenas um dado inserido por vez
  def insert(datum):
    return db[collection].insert_one(datum)

  # método de inserção múltipla, vários dados inseridos por vez
  def bulk_insert(data):
    return db[collection].inser_many(data)

  # exporta o banco atual para o arquivo mongo.json localizado na pasta principal do projeto
  def export():
    pass
