from app.broker.commands.create_route import CreateRoutePayload, CreateRouteValidate
from app.broker.dispatcher  import Dispatcher

import pulsar
from pulsar.schema import *

dispatcher = Dispatcher()

class CommandController:

    def RouteCommandCreate(self, data):
        topic = 'route-command-create'
        payload = CreateRoutePayload(
            order_uuid=str(data['order_uuid']),
            product_uuid=str(data['product_uuid']),
            product_quantity=str(data['product_quantity']),            
            address=str(data['address']),            
        )
        
        comando_integracion = CreateRouteValidate(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(CreateRouteValidate))