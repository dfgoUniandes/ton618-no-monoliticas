
from app.broker.dispatcher  import Dispatcher
import pulsar
from pulsar.schema import *
from app.broker.events.order_completed import OrderCompletedPayload, EventOrderCompleted
from app.broker.events.order_started import OrderStartedPayload, EventOrderStarted
from app.broker.events.product_available import ProductAvailablePayload, EventProductAvailable
from app.broker.events.product_unavailable import ProductUnavailablePayload, EventProductUnavailable
from app.broker.events.route_created import RouteCreatedPayload, EventRouteCreated
from app.broker.events.route_unavailable import RouteUnavailablePayload, EventRouteUnavailable


dispatcher = Dispatcher()

class EventController:

    # Actualizado
    def OrderStartedEvent(self, data):
        topic = 'events-ordenes'
        payload = OrderStartedPayload(
            tag_name='orden-inicializada',            
            order_uuid=str(data['order_uuid']),            
            product_uuid=str(data['product_uuid']),            
            product_quantity=str(data['product_quantity']),            
            order_type=str(data['order_type']),            
            address=str(data['address'])            
        )
        comando_integracion = EventOrderStarted(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(EventOrderStarted))

    # Actualizado
    def OrderCompletedEvent(self, data):
        topic = 'events-ordenes'
        payload = OrderCompletedPayload(
            tag_name='orden-completada',            
            order_uuid=str(data['order_uuid']),            
            route_uuid=str(data['route_uuid']),            
            product_uuid=str(data['product_uuid']),            
            product_quantity=str(data['product_quantity']),            
            order_type=str(data['order_type']),            
            address=str(data['address'])
        )
        comando_integracion = EventOrderCompleted(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(EventOrderCompleted))


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

    def RouteCreatedEvent(self, data):
        topic = 'route-event-created'
        payload = RouteCreatedPayload(
            route_uuid = str(data['route_uuid']),
            order_uuid = str(data['order_uuid']),
            product_uuid = str(data['product_uuid']),
            product_quantity = str(data['product_quantity']),
            address = str(data['address'])           
        )
        comando_integracion = EventRouteCreated(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(EventRouteCreated))

    def RouteUnavailableEvent(self, data):
        topic = 'route-event-unavailable'
        payload = RouteUnavailablePayload(
            order_uuid = str(data['order_uuid']),
            product_uuid = str(data['product_uuid']),
            product_quantity = str(data['product_quantity']),
            address = str(data['address']),          
        )
        comando_integracion = EventRouteUnavailable(data=payload)
        dispatcher._publicar_mensaje(comando_integracion, topic, AvroSchema(EventRouteUnavailable))