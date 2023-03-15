from app.broker.controllers.event_controller import EventController
from app.broker.consumer import suscribirse_a_topico
import asyncio
from app.utils.utils import uuid4Str
from app.broker.commands.create_route import CreateRouteValidate
tasks = list()
event_controller = EventController()


class Domain:

    async def init(self):

        global tasks
        print('Inicializo el dominio de rutas')
        task1 = asyncio.ensure_future(suscribirse_a_topico(
            "coordinar-ruta", "sub-coordinar-ruta-1", CreateRouteValidate, self.process_commands))

        tasks.append(task1)
        # tasks.append(task2)
        await asyncio.sleep(100)

    async def process_commands(self, command, data_command):

        print('Comando a ejecutar: ' + command)

        if command == 'coordinar-ruta':

            global event_controller

            # Logica al recepcionar el comando
            # Interaccion con DB

            data_event_emit = {}
            data_event_emit['route_uuid'] = uuid4Str()
            data_event_emit['order_uuid'] = data_command.order_uuid
            data_event_emit['product_uuid'] = data_command.product_uuid
            data_event_emit['product_quantity'] = data_command.product_quantity
            data_event_emit['order_type'] = data_command.order_type
            data_event_emit['address'] = data_command.address

            event_controller.RouteCreatedEvent(data_event_emit)
