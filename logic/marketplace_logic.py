from persistence import MarketplacePersistence
from persistence.market_place_mongo_db import MarketplaceMongoDB


class MarketplaceSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not MarketplaceSingleton._instance:
            MarketplaceSingleton._instance = object.__new__(cls)
        return MarketplaceSingleton._instance

    def __init__(self):
        db = MarketplaceMongoDB()
        self.db_interface = MarketplacePersistence(db)

    def get_products(self):
        return self.db_interface.get_marketplace_products()

    def get_product(self, product_id):
        return self.db_interface.get_marketplace_product(product_id)

    def add_product(self, product):
        self.db_interface.add_marketplace_product(product)

    def delete_product(self, product_id):
        self.db_interface.delete_marketplace_product(product_id)
