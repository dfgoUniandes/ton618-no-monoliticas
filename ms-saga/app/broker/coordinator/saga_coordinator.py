from app.broker.commands.create_order import CommandCreateOrder

import pulsar, _pulsar
from pulsar.schema import *

client = pulsar.Client('pulsar://localhost:6650')

class Saga_Coordinator:
    
    def init():
        
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