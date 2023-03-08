# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *

from app.broker.events.event_base import Event

class RouteCreatedPayload(Record):
    route_uuid = String()
    order_uuid = String()
    product_uuid = String()
    product_quantity = String()
    address = String()

class EventRouteCreated(Event):
    data = RouteCreatedPayload()