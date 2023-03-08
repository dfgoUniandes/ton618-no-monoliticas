from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, ForeignKey, String, DateTime, Numeric
from sqlalchemy import Enum
from datetime import datetime
from app.utils.utils import uuid4Str
from app import db, ma

class Routes(db.Model):
    uuid = Column(String(40), primary_key=True, default=uuid4Str)
    product_uuid = Column(String(40))
    product_quantity = Column(Numeric)
    vehicle_id = Column(String(10))