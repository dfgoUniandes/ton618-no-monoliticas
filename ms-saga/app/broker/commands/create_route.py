# -*- coding: utf-8 -*-
import pulsar, _pulsar
from pulsar.schema import *

from app.broker.commands.command_base import Command

class CreateRoutePayload(Record):
    order_uuid = String()
    product_uuid = String()
    product_quantity = String()
    address = String()

class CreateRouteValidate(Command):
    data = CreateRoutePayload()