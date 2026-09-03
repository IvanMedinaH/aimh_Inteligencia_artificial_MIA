    ** Agente Dron de inspeccion de infraestructura **
Para poder diseñar un Dron de inspeccion de infraestructura,
bajo el esquema PEAS, pienso que es necesario entender que caracteristicas tiene:

### Agente volador capaz de realizar inspeccion en estructuras de diferentes tipos:
    -capacidad de navegacion area
    -Optimizacion de vuelo considerando distancia y carga
    -percepcion de estructuras
    -diferenciacion de tipos de materiales
    -identificacion de procesos de decaimiento, corrosion, riesgo de derrumbe, otros
    -vuelo autonomo
    -vuelo dirigido asistido
    -potencia de vuelo 
    
    

| Letra | Significado                         | Pregunta guía                                                                             |
|-------|-------------------------------------|-------------------------------------------------------------------------------------------|
| **P** | *Performance* (medida de desempeño) | Autonomia de vuelo/hrs, potencia de vuelo/kw/h, eficiencia de reconocimiento/%,           |
| **E** | *Environment* (entorno)             | Espacio areo definido  y mapeado a coordenadas reales                                     |
| **A** | *Actuators* (actuadores)            | Helices, motores, carcaza, controladora de vuelo, bateria,camaras, sensores de proximidad |
| **S** | *Sensors* (sensores)                | GPS Giroscopio, lidar, sensor de proximidad,magnetometro, Lidar,acelerometro, barometro   |

## Task  Environment:
Vuelo:
Parcialmente observable: se puede decir que el vuelo es parcialmente observable dado que los sensores no proporcionan acceso a todo el estado del vuelo 
Episodico: Secuencial una accion de vuelo encadena la siguiente... preparacion. despegue vuelo, recorrido, aterrizaje etc.
Dinamico: el ambiente puede cambiar de un momento a otro y cada evento puedo ser diferente
Continuo:tiempo de vuelo continuo, una vez iniciado el vuelo el movimiento es continuo, espacio de estados es continuo
no se puede cuantificar el grado de maniobrabilidad requerido en cada vuelo 
single agent : un solo agente esta resolviendo el problema en cada evento
determinismo: estocastico, pero con un grado determinista por los controles de vuelo y los planes de vuelo

Inspector
Parcialmente observable: parcialmente observable, cualquier estructura a inspeccionar se realiza por partes 
Episodico: Secuencial en su movimiento dentro del estado para poder aproximarse o corregir su posicion en caso de errores
Dinamico: El ambiente puede cambiar en iluminacion, presion y direccion del viento por lo que se requiere realizar ajustes
Discreción: Continuo el drop puede estar en inifnitias posiciones de vuelo
single agent : un solo agente esta dedicado al control de la toma de muestras
determinismo: estocastico, se depende de un control de vuelo eficiente y un dia con condiciones controladas



## Performance:
**(how to measure this system)**:

| Dimension a medir                                      | Medido en  |
|--------------------------------------------------------|------------|
| Autonomia de vuelo                                     | hrs - mins |
| potencia de vuelo                                      | kw/h       |
| eficiencia de reconocimiento                           | %          |
| eficiencia en la toma de muestras                      | %          |
| Eficiencia en el seguimiento de la planeacion de vuelo | %          | 
     