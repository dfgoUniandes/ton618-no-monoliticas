from abc import ABC, abstractmethod
from dataclasses import dataclass
import uuid
import datetime
from app.broker.controllers.command_controller import CommandController

command_controller = CommandController()

class Paso():
    id_correlacion: uuid.UUID
    fecha_evento: datetime.datetime
    index: int

@dataclass
class Transaccion(Paso):
    index: int
    comando: any
    comandoCreador: any
    evento: any
    error: any
    compensacion: any
    compensacionCreador: any

class CoordinadorSaga(ABC):
    id_correlacion: uuid.UUID

    def publicar_comando(self, evento, comandoCreador: any, data):
        comandoCreador(data)




@dataclass
class Inicio(Paso):
    index: int = 0

@dataclass
class Fin(Paso):
    ...



class CoordinadorOrdenes(CoordinadorSaga):

    pasos: list()
    index: int

    def inicializar_pasos(self):
        self.pasos = [
            Transaccion(index=0, comando='', comandoCreador='', evento='orden-recibida', error='', compensacion='', compensacionCreador=''),
            Transaccion(index=1, comando='crear-orden', comandoCreador=command_controller.OrderCommandCreator, evento='orden-inicializada', error='creacion-orden-fallida', compensacion='cancelar-orden', compensacionCreador=''),
            Transaccion(index=2, comando='verificar-producto', comandoCreador=command_controller.StockCommandValidator, evento='product-event-available', error='product-event-unavailable', compensacion='cancelar-orden', compensacionCreador=''),
            Transaccion(index=3, comando='coordinar-ruta', comandoCreador=command_controller.RouteCommandCreate, evento='route-event-created', error='route-event-unavailable', compensacion='compensacion-coordinar-ruta', compensacionCreador=''),
            Transaccion(index=4, comando='alistar-producto', comandoCreador=command_controller.ProductCommandPrepare, evento='product-event-ready', error='product-event-unready', compensacion='', compensacionCreador=''),
            Transaccion(index=5, comando='completar-orden', comandoCreador=command_controller.CompleteOrderCommandCreator, evento='orden-completada', error='creacion-orden-fallida', compensacion='cancelar-orden', compensacionCreador=''),
        ]

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...


    def iniciar(self, data):
        # self.persistir_en_saga_log(self.pasos[0])
        self.publicar_comando('crear-orden', self.pasos[1].comandoCreador, data)
        return


    def terminar(self):
        # self.persistir_en_saga_log(self.pasos[-1])
        print('Transaccion Terminada')
        return


    def obtener_paso_dado_un_evento(self, evento: str):
        for i, paso in enumerate(self.pasos):

            if evento == paso.evento or evento == paso.error:
                return paso, i

        raise Exception("Evento no hace parte de la transacción")


    def es_ultima_transaccion(self, index):
        return (len(self.pasos) - 1) == index


    def procesar_evento(self, evento: str, data):
        paso, index = self.obtener_paso_dado_un_evento(evento)
        if index == 0:
            self.iniciar(data)
        elif self.es_ultima_transaccion(index) and not evento == paso.error:
            self.terminar()
        elif evento == paso.error:
            self.publicar_comando(evento, self.pasos[index-1].compensacionCreador, data)
        elif evento == paso.evento:
            self.publicar_comando(evento, self.pasos[index+1].comandoCreador, data)