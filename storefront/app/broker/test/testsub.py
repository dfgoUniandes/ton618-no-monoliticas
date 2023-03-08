import pulsar, _pulsar
from pulsar.schema import *
import uuid
import time
import os

def time_millis():
    return int(time.time() * 1000)

class Command(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class CreateOrderPayload(Record):
    id_producto = String()
    cantidad_producto = String()
    tipo_orden = String()

class CommandCreateOrder(Command):
    data = CreateOrderPayload()

HOSTNAME = os.getenv('PULSAR_ADDRESS', default="localhost")

client = pulsar.Client(f'pulsar://{HOSTNAME}:6650')
consumer = client.subscribe('topico-test', consumer_type=_pulsar.ConsumerType.Shared, subscription_name='sub-notificacion-topico-test', schema=AvroSchema(CommandCreateOrder))

while True:
    msg = consumer.receive()
    print('=========================================')
    print("Mensaje Recibido: '%s'" % msg.value().data)
    print('=========================================')

    print('==== Envía correo a usuario ====')

    consumer.acknowledge(msg)

client.close()