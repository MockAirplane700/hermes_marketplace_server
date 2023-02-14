import json
from flask_restful.utils import cors
from logic.amazon_affiliate_logic import AmazonAffiliateProductsSingleton
from logic.marketplace_logic import MarketplaceSingleton
from flask import Flask, request, render_template, abort, jsonify
from flask_restful import Resource, Api, reqparse
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app)
api = Api(app)

parser = reqparse.RequestParser()


class AmazonProducts(Resource):
    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def get(self):
        db = AmazonAffiliateProductsSingleton()
        result = db.get_products()
        return result

    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def post(self):
        data = request.get_json(force=True)
        print(data)


class MarketplaceProducts(Resource):
    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def get(self):
        db = MarketplaceSingleton()
        result = db.get_products()
        return result

    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def post(self):
        data = request.get_json(force=True)
        print(data)


@app.route('/')
def index_page():
    return render_template("index.html")


api.add_resource(AmazonProducts, '/api/amazon')
api.add_resource(MarketplaceProducts, '/api/marketplace')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, threaded=True)
