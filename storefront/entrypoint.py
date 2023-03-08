from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_cors import CORS
from app import create_app
from flask import jsonify
from flask_migrate import Migrate
from app.views.views import  Health, OrderCreation
import os

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

api = Api(app)
CORS(app)

api.add_resource(Health, "/eda/storefront/v1/health")
api.add_resource(OrderCreation, "/eda/storefront/v1/new-order")

if __name__ == '__main__':
    app.run()