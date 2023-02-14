import pymongo
from persistence.market_place_database import MarketPlaceDatabase
from bson.json_util import dumps
from bson.objectid import ObjectId
from dotenv import load_dotenv
import os

load_dotenv()
url_string = os.getenv('MONGO_URL')


class MarketplaceMongoDB(MarketPlaceDatabase):
    def __init__(self):
        self.db = None
        self.database_name = 'HermesMarketplace'
        self.collection_name = 'marketplace'
        self.collection = None

    def connect_db(self):
        try:
            client = pymongo.MongoClient(url_string)
            temp_db = client[self.database_name]
            return temp_db[self.collection_name]
        except Exception as error:
            print('Failed to connect %s', error)

    def get_all_products(self):
        client = pymongo.MongoClient(url_string)
        temp_db = client['HermesMarketplace']
        product_result = list(temp_db['marketplace'].find())
        result = dumps(product_result)
        return result

    def get_product(self, product_id):
        client = pymongo.MongoClient(url_string)
        temp_db = client['HermesMarketplace']
        amazon_result = temp_db['marketplace'].find_one({'_id': ObjectId(product_id)})
        result = dumps(amazon_result)
        return result

    def add_product(self, product):
        try:
            client = pymongo.MongoClient(url_string)
            temp_db = client['HermesMarketplace']
            temp_db['marketplace'].insert_one(product)
        except Exception as error:
            print('There was an error %s', error)

    def delete_product(self, product_id):
        try:
            client = pymongo.MongoClient(url_string)
            temp_db = client['HermesMarketplace']
            temp_db['marketplace'].delete_one({'_id': ObjectId(product_id)})
        except Exception as error:
            print('There was an error %s', error)