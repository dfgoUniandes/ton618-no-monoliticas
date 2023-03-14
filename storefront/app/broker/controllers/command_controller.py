from app.broker.commands.create_order import CreateOrderPayload, CommandCreateOrder
from app.broker.dispatcher import Dispatcher
import pulsar
from pulsar.schema import *

dispatcher = Dispatcher()

class CommandController:

    def OrderCommandCreator(self, data):
        topico = 'events-storefront'

        payload = CreateOrderPayload(
            event_name='orden-recibida',
            
            product_uuid=str(data['product_uuid']),
            product_quantity=str(data['product_quantity']),
            order_type=str(data['order_type']),
            address=str(data['address'])
        )
        
        comando_integracion = CommandCreateOrder(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topico, AvroSchema(CommandCreateOrder))