from flask_restful import Api
from flask_cors import CORS
from app import create_app
import os
from app.broker.coordinator.saga_coordinator import Saga_Coordinator

saga_coordinator = Saga_Coordinator()

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

api = Api(app)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)

saga_coordinator.init()

    

