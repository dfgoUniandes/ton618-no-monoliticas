
from app.broker.dispatcher  import Dispatcher
import pulsar
from pulsar.schema import *
from app.broker.events.product_available import ProductAvailablePayload, EventProductAvailable
from app.broker.events.product_unavailable import ProductUnavailablePayload, EventProductUnavailable
from app.broker.events.product_ready import ProductReadyPayload, EventProductReady

dispatcher = Dispatcher()

class EventController:

    def ProductAvailableEvent(self, data):
        topic = 'product-event-available'
        payload = ProductAvailablePayload(
            order_uuid = str(data['order_uuid']),
            product_uuid = str(data['product_uuid']),
            product_quantity = str(data['product_quantity'])          
        )
        comando_integracion = EventProductAvailable(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(EventProductAvailable))

    def ProductUnavailableEvent(self,  data):
        topic = 'product-event-unavailable'
        payload = ProductUnavailablePayload(
            order_uuid = str(data['order_uuid']),
            product_uuid = str(data['product_uuid']),
            product_quantity = str(data['product_quantity'])             
        )
        comando_integracion = EventProductUnavailable(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(EventProductUnavailable))

    def ProductReadyEvent(self,  data):
        topic = 'product-event-ready'
        payload = ProductReadyPayload(
            order_uuid = str(data['order_uuid']),
            product_uuid = str(data['product_uuid']),
            product_quantity = str(data['product_quantity'])             
        )
        comando_integracion = EventProductReady(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(EventProductReady))

