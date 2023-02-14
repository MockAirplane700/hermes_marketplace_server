class AmazonAffiliatePersistence:
    def __init__(self, persistence_db):
        self._db = persistence_db

    def get_affiliate_products(self):
        return self._db.get_amazon_products()

    def get_affiliate_product(self, product_id):
        return self._db.get_amazon_product(product_id)

    def add_affiliate_product(self, product):
        self._db.add_amazon_product(product)

    def delete_affiliate_product(self, product_id):
        self._db.delete_amazon_product(product_id)


class MarketplacePersistence:
    def __init__(self, persistence_db):
        self._db = persistence_db

    def get_marketplace_products(self):
        return self._db.get_all_products()

    def get_marketplace_product(self, product_id):
        return self._db.get_product(product_id)

    def add_marketplace_product(self, product):
        self._db.add_product(product)

    def delete_marketplace_product(self, product_id):
        self._db.delete_product(product_id)
