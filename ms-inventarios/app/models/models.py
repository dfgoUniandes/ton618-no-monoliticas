from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, ForeignKey, String, DateTime, Numeric
from sqlalchemy import Enum
from datetime import datetime
from app.utils.utils import uuid4Str
from app import db, ma

class Stock(db.Model):
    product_uuid = Column(String(40), primary_key=True, default=uuid4Str)
    product_quantity = Column(Numeric)