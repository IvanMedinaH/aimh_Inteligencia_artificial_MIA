    ** Vehiculo Autonomo **
Para poder diseñar un vehiculo autonomo,
bajo el esquema PEAS, pienso que es necesario entender que caracteristicas debe cumplir:

### Mecanismo de transporte dirigido por un sistema multi agente:
    -Capacidad de navegacion
    -Cpacidad de reaccion ante obstaculos para acelerar y frenar
    -Capacidad de carga de individuos /objetos
    -Vision periferica en puntos clave 
    -seguridad de pasajero al interior de cabina
    -Potencia de motor
    -Rango de autonomia  para distancias considerables
    -Capacidad, potencia y consumo de carga energetica eficiente


*Nota: reconozco que este sistema de transporte es mucho mas complejo
y contiene infinidad de sistemas interactuando por lo que este PEAS
es meramente didactico para propositos de demostracion del entendimiento
del tema.
    

| Letra | Significado | Pregunta guía                                                                                                                                                                                                                  |
|-------| --- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **P** | *Performance* (medida de desempeño) | * KWH/potencia de carga,<br/>* consumo KWH/KM, <br/>* potencia motor/KW,<br/>* identificacion de peatones/ %, <br/>* Capacidad de carga /cm3 vol <br/>* capacidad de navegacion Eficiencia de trayectoria / %                  |
| **E** | *Environment* (entorno) | *ejercicio pensado para anmbientes de ciudades pequeñas unicamente, con carreteras bien definidas                                                                                                                              |
| **A** | *Actuators* (actuadores) | motor, ruedas, camaras,  bocina, pantallas, odometro digital, freno, acelerador, palancas, botones,                                                                                                                            |
| **S** | *Sensors* (sensores) | +sistema de monitoreo de velocidad,<br/>+ sistema de monitoreo de direccion,<br/>+ sensores de proximidad de peatones,<br/>+ sistema touch en pantallas,<br/>+ sensor de profundidad,<br/>+ sensor de carga <br/> |

## Task  Environment:
**Parcialmente observable:** ya que no se puede conocer, lo que esta sucediendo con los otros vehiculos al rededor o en segmentos de via fuera del rango visual 

**Secuencial:** ya que un evento al conducir puede o no ser producto de la consecuencia, o consecuencia directa de otro

**Dinamico: ** el ambiente puede cambiar de un momento a otro durante la conduccion 

**Continuo:** no se puede cuantificar una velocidad continua por el trafico por ejemplo, o una conduccion en linea recta, por la dispocicion de calles etc. 

**determinismo:** deterministico

**single agent /multi agent:** Un solo agente puede considerarse como el vehiculo, pero los problemas que se estan resolviendo los realizan multiples agentes en el vehiculo



## Performance:
**(how to measure this system)**:

| Dimension a medir          | Medido en    |
|----------------------------|--------------|
| potencia de carga          | KWH          |
| consumo                    | KWH/KM       |
| potencia  motor            | KW           |
| identificacion de peatones | %            |
| capacidad de navegacion Eficiencia de trayectoria | %            |
| Capacidad de carga         | cm3 vol / kg |
