from app.broker.commands.create_order import CommandCreateOrder
from app.broker.consumer import suscribirse_a_topico
import asyncio

tasks = list()

async def init():

    global tasks
    print('Function INIT')
    task1 = asyncio.ensure_future(suscribirse_a_topico("crear-orden", "sub-crear-orden-1", CommandCreateOrder))
    # task2 = asyncio.ensure_future(suscribirse_a_topico("events-storefront", "sub-storefront-2", CommandCreateOrder))
    
    tasks.append(task1)
    # tasks.append(task2)
    await asyncio.sleep(100)
    
