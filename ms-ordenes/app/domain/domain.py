from app.broker.controllers.event_controller import EventController
from app.broker.commands.create_order import CommandCreateOrder
from app.broker.commands.complete_order import CommandCompleteOrder
from app.broker.consumer import suscribirse_a_topico
import asyncio
from app.utils.utils import uuid4Str

tasks = list()
event_controller = EventController()

class Domain:

    async def init(self):

        global tasks
        print('Function INIT')
        task1 = asyncio.ensure_future(suscribirse_a_topico("crear-orden", "sub-crear-orden-1", CommandCreateOrder, self.process_commands))
        task2 = asyncio.ensure_future(suscribirse_a_topico("completar-orden", "sub-completar-orden-1", CommandCompleteOrder, self.process_commands))
        
        tasks.append(task1)
        tasks.append(task2)
        await asyncio.sleep(100)
        
    def process_commands(self, command, data_command):

        print('Command Received: ' + command)

        global event_controller
        if command == 'crear-orden':    
            
            # Logica al recepcionar el comando
            # Interaccion con DB

            data_event_emit = {}
            data_event_emit['order_uuid'] = uuid4Str()
            data_event_emit['product_uuid'] = uuid4Str()
            data_event_emit['product_quantity'] = data_command.product_quantity
            data_event_emit['order_type'] = data_command.order_type
            data_event_emit['address'] = data_command.address

            event_controller.OrderStartedEvent(data_event_emit)


        elif command == 'completar-orden':
            
            # Logica al recepcionar el comando
            # Interaccion con DB

            data_event_emit = {}
            data_event_emit['order_uuid'] = uuid4Str()
            data_event_emit['route_uuid'] = uuid4Str()
            data_event_emit['product_uuid'] = uuid4Str()
            data_event_emit['product_quantity'] = data_command.product_quantity
            data_event_emit['order_type'] = data_command.order_type
            data_event_emit['address'] = data_command.address

            event_controller.OrderCompletedEvent(data_event_emit)

