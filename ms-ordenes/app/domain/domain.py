from app.broker.controllers.event_controller import EventController
from app.broker.consumer import suscribirse_a_topico
import asyncio

tasks = list()
event_controller = EventController()

async def init():

    global tasks
    print('Function INIT')
    task1 = asyncio.ensure_future(suscribirse_a_topico("crear-orden", "sub-crear-orden-1", process_commands))
    # task2 = asyncio.ensure_future(suscribirse_a_topico("events-storefront", "sub-storefront-2", CommandCreateOrder))
    
    tasks.append(task1)
    # tasks.append(task2)
    await asyncio.sleep(100)
    
def process_commands(command, data_command):
    if command == 'crear_evento':
        
        global event_controller
        
        # Logica al recepcionar el comando
        # Interaccion con DB

        data_event_emit = {}
        data_event_emit['order_uuid'] = data_command['order_uuid']
        data_event_emit['product_uuid'] = data_command['product_uuid']
        data_event_emit['product_quantity'] = data_command['product_quantity']
        data_event_emit['order_type'] = data_command['order_type']
        data_event_emit['address'] = data_command['address']

        event_controller.OrderStartedEvent(data_event_emit)

