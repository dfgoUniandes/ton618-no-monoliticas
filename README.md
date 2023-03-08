# Presentación Entrega 4 - Experimentación diseño y construcción de soluciones no monolíticas

## Grupo TON618
Integrantes
Elkin Rativa Ruiz
Jorge Pacheco Rodríguez
Oscar Cortes Medina
Diego Garcia Ortega

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

![Diagramas Arquitectura-ExpDiagrama](https://user-images.githubusercontent.com/78925077/223605270-80a0b54c-ecf0-44cc-8908-f564c47ffbc1.png)

Se desarrollan 3 microservicios con comunicación basada en eventos y comandos. Para ello, se usa Apache Pulsar como broker de eventos.
