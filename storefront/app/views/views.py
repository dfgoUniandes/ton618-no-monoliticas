# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask import request, current_app
import validators
import requests
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
import os
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, create_refresh_token
import datetime
from flask_jwt_extended.view_decorators import jwt_required
from flask_jwt_extended import get_jwt_identity, get_jwt
import json
from app.utils.utils import allowed_file
import app
from app.broker.controllers.event_controller import EventController

event_controller = EventController()


class Health(Resource):
    def get(self):
        data = {
            "message" : "OK"
        }

        return data, 200
    
class OrderCreation(Resource):
    def post(self):
        data = {
            "message" : "OK"
        }

        event_controller.OrderReceivedEvent(request.json)

        return data, 202

