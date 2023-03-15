from app.broker.dispatcher  import Dispatcher
from app.broker.events.order_received import OrderReceivedEvent, OrderReceivedPayload
import pulsar
from pulsar.schema import *

dispatcher = Dispatcher()

class EventController:

    def OrderReceivedEvent(self, data):
        topic = 'events-storefront'

        payload = OrderReceivedPayload(
            tag_name='orden-recibida',
            product_uuid=str(data['product_uuid']),
            product_quantity=str(data['product_quantity']),
            order_type=str(data['order_type']),
            address=str(data['address'])
        )

        event_integration = OrderReceivedEvent(data=payload)
        dispatcher._publicar_mensaje(event_integration, topic, AvroSchema(OrderReceivedEvent))
