# Presentación Entrega 4 - 5 - Experimentación diseño y construcción de soluciones no monolíticas

## Grupo TON618
Integrantes
* Elkin Rativa Ruiz
* Jorge Pacheco Rodríguez
* Oscar Cortes Medina
* Diego Garcia Ortega

# Prueba de concepto (experimentación)

## Atributos de calidad escogidos.

| **Atributo de calidad**   | **Prioridad (L/M/H)** | **Justificación**  |
| ------------------------- | --------------------- | ------------------------------------------------------------------------ |
| Escalabilidad             | Alta                  | El sistema pretende atender un número promedio de pedidos de 196000 diariamente. Pero se esperan picos de trabajo donde los pedidos diarios pueden aumentar hasta los 328000. Se requiere que el sistema sea escalable de manera que ajuste los recursos propios para atender la demanda inmediata reduciendo los desperdicios en recursos subutilizados. |
| Inter-operabilidad        | Alta                  | Se espera que el sistema de CSaaS se integre con sistemas externos en menos de 2 meses. Para lograr la integraciones exitosamente y dentro de los tiempos establecidos se deben proponer componentes exclusivos para este propósito.  |
| Facilidad de Modificación | Medio                 | Se debe reducir el acoplamiento entre las estructuras de datos de sistemas externos y el sistema de EDA, ya que lo anterior produce dificultad para integrar nuevos sistemas. Se debe proponer una arquitectura que favorezca la facilidad de modificación de componentes. Esto se logra a través de patrones como ACL |

## Escenarios de calidad escogidos.

### Escenario 1
![image](https://user-images.githubusercontent.com/78925077/223602167-acb6196f-6909-4e78-9a4b-e10577be6eec.png)

### Escenario 2
![image](https://user-images.githubusercontent.com/78925077/223602437-28112387-255d-4db3-9943-8dcbc282262e.png)

### Escenario 3
![image](https://user-images.githubusercontent.com/78925077/223602552-250d0b05-1134-4589-b20c-f2cbc1cf6d4f.png)

## Diseño de experimentación para validar escenarios de calidad. 

![Diagramas Arquitectura-ExpDiagrama drawio](https://user-images.githubusercontent.com/78925077/225509230-6a8fb5f8-d735-4cb0-9200-6f0a4571bdbb.png)

Se desarrollan 3 microservicios con comunicación basada en eventos y comandos. Para ello, se usa Apache Pulsar como broker de eventos.

## Trabajo implementado

* Elkin Rativa Ruiz   : Tareas con respecto a diseño de experimentacion con patrones
                        Base Microservicio Storefront
                        Pullrequest 1 : [Pullrequest 1](https://github.com/dfgoUniandes/ton618-no-monoliticas/pull/1)
                        Pullrequest 7 : [Pullrequest 7](https://github.com/dfgoUniandes/ton618-no-monoliticas/pull/7)
* Oscar Cortes Medina : Microservicio Rutas
                        Revision de implementacion de version 1: 
                        Pullrequest 2: [Pullrequest 2](https://github.com/dfgoUniandes/ton618-no-monoliticas/pull/2)
                        Pullrequest 9: [Pullrequest 9](https://github.com/dfgoUniandes/ton618-no-monoliticas/pull/9)
* Jorge E. Pachero R. : Microservicio Ordenes
                        Pullrequest 3: [Pullrequest 3](https://github.com/dfgoUniandes/ton618-no-monoliticas/pull/3)
                        Pullrequest 8: [Pullrequest 8](https://github.com/dfgoUniandes/ton618-no-monoliticas/pull/8)
* Diego F. Garcia O   : Microservicio Inventario
                        Pullrequest 4: [Pullrequest 4](https://github.com/dfgoUniandes/ton618-no-monoliticas/pull/4)
                        Pullrequest 6: [Pullrequest 5](https://github.com/dfgoUniandes/ton618-no-monoliticas/pull/6)
                        
## Diagrama TO-BE 

![TOBE DEF](https://user-images.githubusercontent.com/78925077/225508976-1b87b438-1c3b-41b1-b42f-98c2520de8a5.jpg)

### Dominios y subdominios
![TOBE DEF (1)](https://user-images.githubusercontent.com/78925077/225509024-85d26377-d0c1-4f9b-beb8-5e1dc7021bd7.jpg)

## Resultados cuantitativos y cualitativos.
* La lógica de negocio se encuentra en cada microservicio y cada microservicio administra y valida su propio dominio.
* Para el coordinador es necesario saber cuando comienza y termina una transacción local, esto se logra a través de los comandos. 
* La idea del BFF (Storefront) es que sirve como punto de contacto para nuestros usuarios, transformando los llamados creacionales síncronos en publicación de comandos y de forma asíncrona escuchar los eventos de integración de los servicios de backend.

## Conclusiones
* Las sagas son una secuencia de operaciones individuales para manejar procesos de negocios largos. En una arquitectura distribuida, cada operación de la saga es ejecutada en un servicio distinto.
* Los BFFs sirven como servicios de agregación y composición y,  pueden ayudarnos a efectuar los procesos necesarios para la experiencia de usuario requerida para no dejar lógica en las manos de los frontend.
* Implementar un proceso de implementación estandarizado. El proceso de implementación debe ser coherente entre los servicios. Se debe crear un nuevo microservicio con un proceso de implementación ya disponible.

## Comandos de Ejecucion
1- Abrir en el repositorio en Gitpod
2- En una consola ejecutar el broker de Apache Pulsar

* docker run -it -p 6650:6650 -p 8080:8080 --mount source=pulsardata,target=/pulsar/data --mount source=pulsarconf,target=/pulsar/conf apachepulsar/pulsar:2.11.0 bin/pulsar standalone

3- Para ejecutar el storefront seguir hacer lo siguiente:
  - Navegar a la carpeta de storefront
  - Ejecutar los comandos:
    * pip install -r requirements.txt
    * export FLASK_APP=entrypoint.py
    * flask run -p 5000
    
4- Para ejecutar el saga seguir hacer lo siguiente:
  - Navegar a la carpeta de saga
  - Ejecutar los comandos:
    * pip install -r requirements.txt
    * export FLASK_APP=entrypoint.py
    * flask run -p 5001
    
5- Para ejecutar el servicio de ordenes seguir hacer lo siguiente:
  - Navegar a la carpeta de ordenes
  - Ejecutar los comandos:
    * pip install -r requirements.txt
    * export FLASK_APP=entrypoint.py
    * flask run -p 5002
        
6- Para ejecutar el servicio de inventario seguir hacer lo siguiente:
  - Navegar a la carpeta de inventario
  - Ejecutar los comandos:
    * pip install -r requirements.txt
    * export FLASK_APP=entrypoint.py
    * flask run -p 5003
        
7- Para ejecutar el servicio de rutas seguir hacer lo siguiente:
  - Navegar a la carpeta de ordenes
  - Ejecutar los comandos:
    * pip install -r requirements.txt
    * export FLASK_APP=entrypoint.py
    * flask run -p 5004


