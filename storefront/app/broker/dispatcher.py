# -*- coding: utf-8 -*-

import pulsar
from pulsar.schema import *

from app.broker.commands.create_order import CreateOrderPayload, CommandCreateOrder

import datetime

epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Dispatcher:
    def _publicar_mensaje(self, mensaje, topico, schema):
        cliente = pulsar.Client(f'pulsar://localhost:6650')
        publicador = cliente.create_producer(topico, schema=schema)
        publicador.send(mensaje)
        cliente.close()
