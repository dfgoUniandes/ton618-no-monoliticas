# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *

from app.broker.events.event_base import Event

class OrderStartedPayload(Record):
    order_uuid = String()

class EventOrderStarted(Event):
    data = OrderStartedPayload()