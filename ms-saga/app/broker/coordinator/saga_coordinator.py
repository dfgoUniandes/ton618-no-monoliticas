from app.broker.commands.create_order import CommandCreateOrder
from app.broker.consumer import suscribirse_a_topico

import pulsar, _pulsar
from pulsar.schema import *
import asyncio

client = pulsar.Client('pulsar://localhost:6650')

class Saga_Coordinator:
    
    def init(self):

        task1 = asyncio.ensure_future(suscribirse_a_topico("events-storefront", "sub-storefront", CommandCreateOrder))
    
        
        # topics = [
        #     {'topic': 'events-storefront', 'subscription': 'sub1', 'schema_type': AvroSchema(CommandCreateOrder)}
        # ]

        # consumers = []
        # for topic in topics:
        #     consumer = client.subscribe(topic=topic['topic'], subscription_name=topic['subscription'], consumer_type=_pulsar.ConsumerType.Shared, schema=topic['schema_type'])
        #     consumers.append(consumer)

        # while True:
        #     for consumer in consumers:
        #         msg = consumer.receive()
        #         try:
        #             print('=========================================')
        #             print("Mensaje Recibido: '%s'" % msg.topic_name())
        #             print("Data Recibida: '%s'" % msg.value().data)
        #             print('=========================================')

        #             consumer.acknowledge(msg)

        #         except:
        #             consumer.negative_acknowledge(msg)