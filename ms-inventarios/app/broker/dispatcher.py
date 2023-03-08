# -*- coding: utf-8 -*-

import pulsar
from pulsar.schema import *

import datetime
epoch = datetime.datetime.utcfromtimestamp(0)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

class Dispatcher:
    def _publicar_mensaje(self, mensaje, topic, schema):
        client = pulsar.Client(f'pulsar://localhost:6650')
        publisher = client.create_producer(topic, schema=schema)
        publisher.send(mensaje)
        client.close()
