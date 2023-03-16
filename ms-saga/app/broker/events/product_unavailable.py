# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *

from app.broker.events.event_base import Event

class ProductUnavailablePayload(Record):
    order_uuid = String()
    product_uuid = String()
    product_quantity = String()

class EventProductUnavailable(Event):
    data = ProductUnavailablePayload()