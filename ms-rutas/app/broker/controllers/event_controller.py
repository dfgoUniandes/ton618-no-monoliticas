
from app.broker.dispatcher  import Dispatcher
import pulsar
from pulsar.schema import *
from app.broker.events.route_created import RouteCreatedPayload, EventRouteCreated
from app.broker.events.route_unavailable import RouteUnavailablePayload, EventRouteUnavailable


dispatcher = Dispatcher()

class EventController:

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