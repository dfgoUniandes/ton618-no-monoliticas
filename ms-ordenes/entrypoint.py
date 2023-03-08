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
    product_uuid = String()
    product_quantity = String()
    order_type = String()
    address = String()

class CommandCreateOrder(Command):
    data = CreateOrderPayload()


class StockValidaterPayload(Record):
    product_uuid = String()
    product_quantity = String()

class CommandStockValidate(Command):
    data = StockValidaterPayload()



if __name__ == '__main__':
    app.run(debug=True)


client = pulsar.Client('pulsar://localhost:6650')

topics = [
    {'topic': 'order_command_create', 'subscription': 'sub1', 'schema_type': AvroSchema(CommandCreateOrder)},
    {'topic': 'productos', 'subscription': 'sub2', 'schema_type': AvroSchema(CommandStockValidate)}
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
            print('=========================================')

            if msg.topic_name() == 'persistent://public/default/order_command_create':
                print('envia el stock')
                orden_data = msg.value().data
                data = {
                    'product_uuid' : orden_data.product_uuid,
                    'product_quantity' : orden_data.product_quantity,
                }
                commandController.StockCommandValidator(data)
                consumer.acknowledge(msg)

            if msg.topic_name() == 'persistent://public/default/productos':
                print('productos validos')
                stock_data = msg.value().data
                data = {
                    'product_uuid' : stock_data.product_uuid,
                    'product_quantity' : stock_data.product_quantity,
                }
                commandController.RouteCommandCreate(data)
                consumer.acknowledge(msg)

        except:
            consumer.negative_acknowledge(msg)
    

client.close()

