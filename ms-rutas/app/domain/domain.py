from app.models.models import db, ma, Routes
from app.broker.controllers.event_controller import EventController
from app.broker.consumer import suscribirse_a_topico
import asyncio
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
            if self.validate_address(data_command):
                route_id = await self.create_route(data_command)
                await self.create_success_emit_event(route_id, data_command)
            else:
                await self.create_error_emit_event(data_command)

        if command == 'compensacion-coordinar-ruta':
            await self.compensate_create_route(data_command)

    async def validate_address(self, data) -> bool:
        return data.address != ""

    async def create_route(self,  data_command) -> str:
        try:
            route = Routes(
                product_uuid=data_command.product_uuid,
                product_quantity=data_command.product_quantity,
                address=data_command.address)
            db.session.add(route)
            db.session.commit()
            return str(route.uuid)
        except Exception:
            self.create_error_emit_event(data_command)
        finally:
            db.session.close()

    async def delete_route(self, route_id):
        try:
            route = Routes.query.filter_by(uuid=route_id).first()
            db.session.delete(route)
            db.session.commit()
        except Exception as e:
            print(e)
        finally:
            db.session.close()

    async def create_success_emit_event(self, route_id, data_command):
        data_event_emit = {}
        data_event_emit['route_uuid'] = route_id
        data_event_emit['order_uuid'] = data_command.order_uuid
        data_event_emit['product_uuid'] = data_command.product_uuid
        data_event_emit['product_quantity'] = data_command.product_quantity
        data_event_emit['order_type'] = data_command.order_type
        data_event_emit['address'] = data_command.address

        event_controller.RouteCreatedEvent(data_event_emit)

    async def create_error_emit_event(self, data_command):
        route_unavailable_event = {}
        route_unavailable_event['order_uuid'] = data_command.order_uuid
        route_unavailable_event['product_uuid'] = data_command.product_uuid
        route_unavailable_event['product_quantity'] = data_command.product_quantity
        route_unavailable_event['address'] = data_command.address

        event_controller.RouteUnavailableEvent(route_unavailable_event)

    async def compensate_create_route(self, data_command):
        print('Compensacion de la creacion de la ruta')
        route_compensated_event = {}
        route_compensated_event['route_uuid'] = data_command.route_uuid
        event_controller.RouteCompensatedEvent(route_compensated_event)
