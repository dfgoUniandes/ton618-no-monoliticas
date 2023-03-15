# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *

from app.broker.events.event_base import Event

class OrderStartedPayload(Record):
    event_name = String()
    order_uuid = String()
    product_uuid = String()
    product_quantity = String()
    order_type = String()
    address = String()

class EventOrderStarted(Event):
    data = OrderStartedPayload()