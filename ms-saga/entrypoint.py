from flask_restful import Api
from flask_cors import CORS
from app import create_app
import pulsar, _pulsar
from pulsar.schema import *
import os
import uuid
import time
from app.broker.controllers.command_controller import CommandController

commandController = CommandController()

settings_module = os.getenv('APP_SETTINGS_MODULE')
app = create_app(settings_module)

api = Api(app)
CORS(app)

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
    event_name = String()
    product_uuid = String()
    product_quantity = String()
    order_type = String()
    address = String()

class CommandCreateOrder(Command):
    data = CreateOrderPayload()



if __name__ == '__main__':
    app.run(debug=True)


client = pulsar.Client('pulsar://localhost:6650')

topics = [
    {'topic': 'order_command_create', 'subscription': 'sub1', 'schema_type': AvroSchema(CommandCreateOrder)}
    ]

consumers = []
for topic in topics:
    consumer = client.subscribe(topic=topic['topic'], subscription_name=topic['subscription'], consumer_type=_pulsar.ConsumerType.Shared, schema=topic['schema_type'])
    consumers.append(consumer)
    


while True:
    for consumer in consumers:
        msg = consumer.receive()
        try:
            print('=========================================')
            print("Mensaje Recibido: '%s'" % msg.topic_name())
            print("Data Recibida: '%s'" % msg.value().data)
            print('=========================================')

            consumer.acknowledge(msg)

        except:
            consumer.negative_acknowledge(msg)
    

