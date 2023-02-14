from persistence import AmazonAffiliatePersistence
from persistence.amazon_affilliate_products_mongo_db import AmazonAffiliateMongoDB


class AmazonAffiliateProductsSingleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not AmazonAffiliateProductsSingleton._instance:
            AmazonAffiliateProductsSingleton._instance = object.__new__(cls)
        return AmazonAffiliateProductsSingleton._instance

    def __init__(self):
        db = AmazonAffiliateMongoDB()
        self.db_interface = AmazonAffiliatePersistence(db)

    def get_products(self):
        return self.db_interface.get_affiliate_products()

    def get_product(self, product_id):
        return self.db_interface.get_affiliate_product(product_id)

    def add_product(self, product):
        self.db_interface.add_affiliate_product(product)

    def delete_product(self, product_id):
        self.db_interface.delete_affiliate_product(product_id)
