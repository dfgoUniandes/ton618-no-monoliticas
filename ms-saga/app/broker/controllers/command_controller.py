from app.broker.commands.create_order import CreateOrderPayload, CommandCreateOrder
from app.broker.commands.stock_validate import StockValidaterPayload, CommandStockValidate
from app.broker.commands.create_route import CreateRoutePayload, CreateRouteValidate
from app.broker.commands.prepare_product import PrepareProductPayload, CommandPrepareProduct
from app.broker.dispatcher  import Dispatcher

import pulsar
from pulsar.schema import *

dispatcher = Dispatcher()

class CommandController:

    def OrderCommandCreator(self, data):
        topico = 'order-command-create'
        payload = CreateOrderPayload(
            # product_uuid=str(data['product_uuid']),
            # product_quantity=str(data['product_quantity']),
            # order_type=str(data['order_type']),
            # address=str(data['address'])
            product_uuid=str(data.product_uuid),
            product_quantity=str(data.product_quantity),
            order_type=str(data.order_type),
            address=str(data.address)
        )
        
        comando_integracion = CommandCreateOrder(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topico, AvroSchema(CommandCreateOrder))


    def StockCommandValidator(self, data):
        topic = 'product-command-validateStock'
        payload = StockValidaterPayload(
            order_uuid=str(data['order_uuid']),
            product_uuid=str(data['product_uuid']),
            product_quantity=str(data['product_quantity']),            
        )
        
        comando_integracion = CommandStockValidate(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(CommandStockValidate))


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


    def ProductCommandPrepare(self, data):
        topic = 'product-command-prepareProduct'
        payload = PrepareProductPayload(
            order_uuid=str(data['order_uuid']),
            product_uuid=str(data['product_uuid']),
            product_quantity=str(data['product_quantity']),            
        )
        
        comando_integracion = CommandPrepareProduct(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(CommandPrepareProduct))