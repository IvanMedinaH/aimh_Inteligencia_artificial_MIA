    ** Robot aspiradora **
Para poder diseñar un Robot aspiradora,
bajo el esquema PEAS, pienso que es necesario entender que caracteristicas tiene:

### Robot capaz de realizar la tarea domestica para limpiar suelos teniendo:
    -capacidad de navegacion
    -potencia de succion
    -capacidad de recoger solidos y liquidos
    -capacidad de carga y eficiencia energetica
    -diferentes programas de limpieza 
    -controlar dispositivo a distancia
    -autonomia de recarga
    

| Letra | Significado | Pregunta guía                                                                                                                                                                                                                        |
| --- | --- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **P** | *Performance* (medida de desempeño) | grado de limpieza, grado de uso de carga/tiempo de ejecucion, limpieza de area delimitada con multiples cepillos incorporados, seguimiento de patrones                                                                               |
| **E** | *Environment* (entorno) | comercial, domestico, industrial, pisos, paredes, techos, de diferentes superficies y materiales                                                                                                                                     |
| **A** | *Actuators* (actuadores) | cepillos,  mangueras, camaras, ruedas, servos, motor de sucion,contenedor de desperdicio, dispositivo bluetooth, pantalla nivel de carga                                                                                             |
| **S** | *Sensors* (sensores) | camara de profundidad, sistema de monitoreo de limpieza, sistema de monitoreo de movimiento, sistema de monitoreo de carga, sistema de monitoreo de posicion, sistema de monitoreo de almacenamiento, sistema de comunicacion remota |

## Environment task:
Parcialmente observable: ya que no se puede conocer todo lo que esta sucio en el espacio delimitado
Episodico: ya que un evento no depende del anterior
Dinamico: el ambiente puede cambiar de un momento a otro y cada evento puedo ser diferente
Continuo: no se puede cuantificar el grado de suciedad por medio de una cantidad
single agent : un solo agente esta resolviendo el problema en cada evento
determinismo: deterministico

## Performance:
**(how to measure this system)**:

| Dimension a medir        | Medido en                                                                                                                                     |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Cantidad de eventos      | unidades configurables (1,2,3,4,5) pasadas x dia                                                                                              |
| intensividad de limpieza | grados, que indican el numero de pasadas x evento (1,2,3)                                                                                     |
| Mayor intensividad       | uso de carga mas elevado (mha - milliamper-hour)                                                                                              |
| patrones de seguimiento  | seguimiento de patrones programado en el celular (opcion de configuracion para espacios delimitados cuadrados/rectangulares)                  |
| tipos de cepillo         | depende del grado seleccionado, puede hacer uso de cepillos diferentes   (aunque no es una medida, el tipo de cepillo puede hacer mas optimo) |