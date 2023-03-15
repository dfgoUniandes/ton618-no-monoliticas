from app.broker.commands.create_order import CommandCreateOrder
from app.broker.consumer import suscribirse_a_topico
from app.saga.saga_ordenes import CoordinadorOrdenes

import pulsar, _pulsar
from pulsar.schema import *
import asyncio

client = pulsar.Client('pulsar://localhost:6650')
tasks = list()

class Saga_Coordinator:

    coordinador_ordenes = CoordinadorOrdenes()

    async def init(self):

        self.coordinador_ordenes.inicializar_pasos()

        global tasks
        print('Function INIT')
        task1 = asyncio.ensure_future(suscribirse_a_topico("events-storefront", "sub-storefront-1", CommandCreateOrder, self.coordinador_ordenes))
        # task2 = asyncio.ensure_future(suscribirse_a_topico("events-storefront", "sub-storefront-2", CommandCreateOrder))
        
        tasks.append(task1)
        # tasks.append(task2)
        await asyncio.sleep(100)
