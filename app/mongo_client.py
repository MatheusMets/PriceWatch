from pymongo import MongoClient

class MongoDB:

  client = MongoClient()

  def get_client():
    return client




