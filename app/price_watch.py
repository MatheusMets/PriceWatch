from mongo_client import MongoClient

class PriceWatch:

  def main():
    mongo = MongoClient.get_client()
    db = mongo.price_watch
    collection = db.products
