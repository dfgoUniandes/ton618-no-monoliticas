from app.broker.controllers.event_controller import EventController
from app.broker.commands.prepare_product import CommandPrepareProduct
from app.broker.commands.stock_validate import CommandStockValidate
from app.broker.consumer import suscribirse_a_topico
import asyncio
from app.utils.utils import uuid4Str

tasks = list()
event_controller = EventController()

class Domain:

    async def init(self):

        global tasks
        print('Function INIT')
        task1 = asyncio.ensure_future(suscribirse_a_topico("verificar-producto", "sub-verificar-prod", CommandStockValidate, self.process_commands))
        task2 = asyncio.ensure_future(suscribirse_a_topico("alistar-producto", "sub-alistar-prod", CommandPrepareProduct, self.process_commands))
        
        tasks.append(task1)
        tasks.append(task2)
        await asyncio.sleep(100)
        
    def process_commands(self, command, data_command):

        print('Command: ' + command)
        print('data: ' + data_command)

        if command == 'verificar-producto':
            
            global event_controller
            
            # Logica al recepcionar el comando
            # Interaccion con DB

            data_event_emit = {}
            data_event_emit['order_uuid'] = uuid4Str()
            data_event_emit['product_uuid'] = data_command.product_uuid
            data_event_emit['product_quantity'] = data_command.product_quantity
            data_event_emit['order_type'] = data_command.order_type
            data_event_emit['address'] = data_command.address

            event_controller.ProductAvailableEvent(data_event_emit)

        if command == 'alistar-producto':
            global event_controller
            
            # Logica al recepcionar el comando
            # Interaccion con DB

            data_event_emit = {}
            data_event_emit['order_uuid'] = uuid4Str()
            data_event_emit['product_uuid'] = data_command.product_uuid
            data_event_emit['product_quantity'] = data_command.product_quantity
            data_event_emit['order_type'] = data_command.order_type
            data_event_emit['address'] = data_command.address

            event_controller.ProductReadyEvent(data_event_emit)

