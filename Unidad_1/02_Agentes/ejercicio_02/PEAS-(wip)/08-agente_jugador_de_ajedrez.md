    ** Agente Jugador de ajedrez **
Para poder diseñar un agente que pueda Jugar ajedrez,
bajo el esquema PEAS, pienso que es necesario entender que caracteristicas tiene:

### Agente volador capaz de realizar inspeccion en estructuras de diferentes tipos:
    -Conocimiento de Jugadas
    -Planeacion extensa de movimientos hacia el futuro
    -Conocimiento de los componetes del tablero
    -Conocimiento de las fichas de ajedrez y sus movimientos
    -Capacidad de reaccion a jugadas
      

| Letra | Significado                         | Pregunta guía                                                                                                                                                                              |
|-------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **P** | *Performance* (medida de desempeño) | Eficiencia de juegos ganados / % ,Cantidad de fichas ganadas, juegos jugados, tipo de fichas ganadas por Juego                                                                             |
| **E** | *Environment* (entorno)             | Tablero de ajedrez, jugadas, estado del tablero en cada jugada                                                                                                                             |
| **A** | *Actuators* (actuadores)            | softbot(awereness de las casillas y el estado del tablero), funcion de control por turno, funcion de jugada o lanzamiento, funcion de planificacion, funcion de decision optima por jugada |
| **S** | *Sensors* (sensores)                | Loop manager(controla los turnos), game score(controla las estadisticas del juego), game manager(visor del juego en modo dios)                                                             |

## Task  Environment:
Observable: Todo el estado del tablero esta a la vista siempre 
Episodico: Secuencial una accion encadena la siguiente... por medio de las jugadas y la planeacion 
Dinamica: Estatica  
Discrecion: Discreto, hay un numero finito de jugadas  
Multi agent : al ser un juego diseñado para jugarse entre 2 puede haber minimo 1 agente y un humano o 2 agentes en el juego
determinismo: Deterministico, a pesar de la incertidumbre, la consecuencia
de ir abordando las jugadas con maestria, el resultado es el  mismo para la N-sima jugada
donde el resultado puede definir al ganador.

*nota: a pesar de que puede existir una componente de incertidumbre hacia la siguiente jugada
durante el juego, siempre las jugadas especificas determinaran al ganador.


## Performance:
**(how to measure this system)**:

| Dimension a medir                | Medido en                                     |
|----------------------------------|-----------------------------------------------|
| Eficiencia de juegos ganados     | %                                             |
| juegos jugados                   | 0-99999                                       |
| tipo de fichas ganadas por Juego | [(Al,0),(Re,0),(Rn,0),(Cbll,0),(Trr,0),(P,0)] |
| Torneos ganados                  | 0                                             |
|                                  |                                               | 

 ,Cantidad de Fichas ganadas, juegos jugados, tipo de fichas ganadas por Juego