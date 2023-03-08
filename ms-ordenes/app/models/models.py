from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, ForeignKey, String, DateTime, Numeric
from sqlalchemy import Enum
from datetime import datetime
from app.utils.utils import uuid4Str
from .enums import *
from app import db, ma

class Order(db.Model):
    uuid = Column(String(40), primary_key=True, default=uuid4Str)
    order_type = Column(String(40))
    product_uuid = Column(String(40))
    product_quantity = Column(String(40))