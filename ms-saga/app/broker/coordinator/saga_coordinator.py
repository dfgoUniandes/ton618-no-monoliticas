from app.broker.events.order_received import OrderReceivedEvent
from app.broker.events.order_started import EventOrderStarted
from app.broker.events.route_created import EventRouteCreated
from app.broker.events.route_unavailable import EventRouteUnavailable
from app.broker.events.route_compensated import EventRouteCompensated
from app.broker.consumer import suscribirse_a_topico
from app.saga.saga_ordenes import CoordinadorOrdenes
import asyncio

tasks = list()

class Saga_Coordinator:

    coordinador_ordenes = CoordinadorOrdenes()

    async def init(self):

        self.coordinador_ordenes.inicializar_pasos()

        global tasks
        print('Function INIT')
        task1 = asyncio.ensure_future(suscribirse_a_topico("events-storefront", "sub-storefront-1", OrderReceivedEvent, self.coordinador_ordenes))
        task2 = asyncio.ensure_future(suscribirse_a_topico("events-ordenes", "sub-ordenes-1", EventOrderStarted, self.coordinador_ordenes))
        task2 = asyncio.ensure_future(suscribirse_a_topico("route-event-created", "sub-rutas-1", EventRouteCreated, self.coordinador_ordenes))
        task2 = asyncio.ensure_future(suscribirse_a_topico("route-event-unavailable", "sub-rutas-2", EventRouteUnavailable, self.coordinador_ordenes))
        task2 = asyncio.ensure_future(suscribirse_a_topico("route-event-compensated", "sub-rutas-3", EventRouteCompensated, self.coordinador_ordenes))
        
        tasks.append(task1)
        tasks.append(task2)
        await asyncio.sleep(100)
