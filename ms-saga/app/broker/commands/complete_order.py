# -*- coding: utf-8 -*-

import pulsar, _pulsar
from pulsar.schema import *

from app.broker.commands.command_base import Command

class CompleteOrderPayload(Record):
    
    tag_name = String()
    product_uuid = String()
    product_quantity = String()
    order_type = String()
    route_uuid = String()
    address = String()

class CommandCompleteOrder(Command):
    data = CompleteOrderPayload()