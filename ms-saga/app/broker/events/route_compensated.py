# -*- coding: utf-8 -*-

import pulsar
import _pulsar
from pulsar.schema import *

from app.broker.events.event_base import Event


class RouteCompensatedPayload(Record):
    route_uuid = String()


class EventRouteCompensated(Event):
    data = RouteCompensatedPayload()
