# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *

from app.broker.events.event_base import Event

class OrderReceivedPayload(Event):
    event_name = String()
    product_uuid = String()
    product_quantity = String()
    order_type = String()
    address = String()

class OrderReceivedEvent(Event):
    data = OrderReceivedPayload()