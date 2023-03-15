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

    def publicar_comando(self, evento, comandoCreador: any):
        comandoCreador()
    


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
            Transaccion(index=1, comando='crear-orden', comandoCreador=command_controller.OrderCommandCreator, evento='OrdenInicializada', error='CreacionOrdenFallida', compensacion='CancelarOrden', compensacionCreador=''),
        ]

    def persistir_en_saga_log(self, mensaje):
        # TODO Persistir estado en DB
        # Probablemente usted podría usar un repositorio para ello
        ...
    

    def iniciar(self):
        # self.persistir_en_saga_log(self.pasos[0])
        self.publicar_comando('CrearOrden', self.pasos[1].comandoCreador)
        return


    def terminar(self):
        # self.persistir_en_saga_log(self.pasos[-1])
        return


    def obtener_paso_dado_un_evento(self, evento: str):
        for i, paso in enumerate(self.pasos):

            if evento == paso.evento or evento == paso.error:
                return paso, i
            
        raise Exception("Evento no hace parte de la transacción")
                

    def es_ultima_transaccion(self, index):
        return (len(self.pasos) - 1) == index


    def procesar_evento(self, evento: str):
        paso, index = self.obtener_paso_dado_un_evento(evento)
        if index == 0:
            self.iniciar()
        elif self.es_ultima_transaccion(index) and not evento == paso.error:
            self.terminar()
        elif evento == paso.error:
            self.publicar_comando(evento, self.pasos[index-1].compensacionCreador)
        elif isinstance(evento, paso.evento):
            self.publicar_comando(evento, self.pasos[index+1].comandoCreador)