# coding: utf-8
from pymongo import MongoClient

# classe intermediária entre o banco de dados e os scripts
class MongoDB:

  # variável contendo o banco
  def __init__(self):
    self.client = MongoClient()
    self.db = self.client.PriceWatch

  # método de inserção simples, apenas um dado inserido por vez
  def insert(self, datum):
    return self.db.products.insert_one(datum)

  # método de inserção múltipla, vários dados inseridos por vez
  def bulk_insert(data):
    return self.db.products.inser_many(data)

  # exporta o banco atual para o arquivo mongo.json localizado na pasta principal do projeto
  def export():
    pass
