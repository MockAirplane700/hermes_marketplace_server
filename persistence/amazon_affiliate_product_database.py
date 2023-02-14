from abc import ABC, abstractmethod


class AmazonAffiliateProductDatabase(ABC):
    @abstractmethod
    def connect_db(self):
        pass

    @abstractmethod
    def get_amazon_products(self):
        return None

    @abstractmethod
    def get_amazon_product(self, product_id):
        return None

    @abstractmethod
    def add_amazon_product(self, product):
        pass

    @abstractmethod
    def delete_amazon_product(self, product_id):
        pass
