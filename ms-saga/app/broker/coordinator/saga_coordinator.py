from app.broker.events.order_received import OrderReceivedEvent
from app.broker.events.order_started import EventOrderStarted
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
        task2 = asyncio.ensure_future(suscribirse_a_topico("events-ordenes", "sub-ordenes-1", EventOrderStarted))
        
        tasks.append(task1)
        tasks.append(task2)
        await asyncio.sleep(100)
