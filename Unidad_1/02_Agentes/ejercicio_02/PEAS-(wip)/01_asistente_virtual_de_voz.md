    ** Asistente virtual de voz **
Para poder diseñar un asistente virtual de voz,
bajo el esquema PEAS, pienso que es necesario entender que son:

### Programa software que:
    -responde a comandos hablados para realizar tareas
    -buscar información 
    -controlar dispositivos.


| Letra | Significado | Pregunta guía                                                                                                                                                                                                                                                                  |
| --- | --- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **P** | *Performance* (medida de desempeño) | -Interactua con otras apps,<br/>-utiliza el idioma del usuario, <br/>-capta la voz del usuario desde diferentes rangos y volumenes,<br/>- Es altamente responsivo <br/>- puede conectarse a la red,<br/>- responde en varios idiomas,<br/>- alta fidelidad en streams de audio |
| **E** | *Environment* (entorno) | mobil/ Escritorio/ web / Gadgets, usando sus canales de sonido y recepcion de audio                                                                                                                                                                                            |
| **A** | *Actuators* (actuadores) | -Microfono, <br/>-bocinas, <br/>-herramientas de su sistema operativo,<br/>-gestor de archivos, <br/>-monitor de alarmas, <br/>-sistema de notificaciones, <br/>-sistema de red, <br/>-sistema administrador de recursos del SO <br/>-dispositivos externos conectados         |
| **S** | *Sensors* (sensores) | -Microfono, <br/>-sistema monitor de hora del sistema, <br/>-sistema monitor de notificaciones, <br/>-dispositivos externos conectados via red o harware                                                                                                                       |

NOTA:* la naturaleza de los actuadores utilizados, les permitira ser
tanto actuador como sensor en este caso el microfono y las bocinas
(transductor reversible).

## Environment Task:
**Parcialmente observable**: ya que no se puede conocer que solicitara el usuario en donde opera este agente del medio auditivo, 
aunque existe un rango definido de las capacidades del asistente, por lo que tampoco puede realizar actividades fuera de ese rango

**Episodico/secuencial**: ya que un evento no depende del anterior, un usuario puede solicitar una tarea que tenga consecuencias 

**Dinamico**: el ambiente puede cambiar de un momento a otro y cada evento puedo ser diferente

**Continuo**: no se puede cuantificar el grado de claridad con la que el usuario habla
al dispositivo por lo que podria fallar si no entiende en la interaccion


## Performance:
**(how to measure this system)**: 

|Dimension a medir| Medido en:                                                                                                         |
|---|--------------------------------------------------------------------------------------------------------------------|
|Interactua con otras apps| intents:es capaz de identificar que app puede realizar la tarea para la cual se lanzo el comando. conexion a APIS, |
|Capta la voz del usuario desde diferentes rangos y volumenes| bajo diferentes volumenes de voz y en distancias considerables puede reconocer los comandos del usuario            |
|Es altamente responsivo| el tiempo de respuesta esta por debajo de los 3 segundos para multiples comandos                                   |
|Puede conectarse a la red| utiliza protocolos de red WIFI /Ethernet                                                                           |
|Responde en varios idiomas| es posible interactuar en todos los niveles desde varios idiomas                                                   |
|Alta fidelidad en streams de audio| la calidad del audio (Khtz) es verificable, es capaz de procesar en diferentes rangos de bitrate para streams |  