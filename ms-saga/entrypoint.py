from flask_restful import Api
from flask_cors import CORS
from app import create_app
import os
from app.broker.coordinator.saga_coordinator import Saga_Coordinator

from app.broker.commands.create_order import CommandCreateOrder
from app.broker.consumer import suscribirse_a_topico

import asyncio

saga_coordinator = Saga_Coordinator()

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

api = Api(app)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)


with app.app_context():
    asyncio.run(saga_coordinator.init())

# @app.before_first_request
# async def init(self):
#     print('Function INIT')
#     task1 = asyncio.ensure_future(suscribirse_a_topico("events-storefront", "sub-storefront", CommandCreateOrder))
    

