from abc import ABC, abstractmethod


class MarketPlaceDatabase(ABC):
    @abstractmethod
    def connect_db(self):
        pass

    @abstractmethod
    def get_all_products(self):
        return None

    @abstractmethod
    def get_product(self, product_id):
        return None

    @abstractmethod
    def add_product(self, product):
        pass

    @abstractmethod
    def delete_product(self, product_id):
        pass
