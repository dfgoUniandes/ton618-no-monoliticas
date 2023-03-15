from app.broker.commands.create_order import CreateOrderPayload, CommandCreateOrder
from app.broker.dispatcher import Dispatcher
import pulsar
from pulsar.schema import *

dispatcher = Dispatcher()

class CommandController:
    ...