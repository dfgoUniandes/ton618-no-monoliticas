from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from app.broker.coordinator.saga_coordinator import Saga_Coordinator
import asyncio
saga_coordinator = Saga_Coordinator()

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()

def create_app(settings_module):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(settings_module)
    if not app.config.get('TESTING', False):
        app.config.from_pyfile('production.py', silent=True)
    else:
        app.config.from_pyfile('testqa.py', silent=True)

    db.init_app(app)
    # migrate.init_app(app, db, render_as_batch=True)
    with app.app_context():
        db.create_all()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(saga_coordinator.init())

    return app