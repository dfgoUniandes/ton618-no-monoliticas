# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *

from app.broker.events.event_base import Event

class OrderCompletedPayload(Record):
    
    tag_name = String()
    product_uuid = String()
    product_quantity = String()
    order_type = String()
    route_uuid = String()
    address = String()

class EventOrderCompleted(Event):
    data = OrderCompletedPayload()