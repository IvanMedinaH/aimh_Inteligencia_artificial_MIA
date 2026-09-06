# Structure of agents

`Agent  = Arquitecture + Program`

**La Arquitectura:**
Es la maquinaria física o el entorno de ejecución (sensores, actuadores, hardware, 
computadores).

**El Programa de Agente (Agent Program):** 
Es la implementación concreta del algoritmo, la función matemática que corre sobre 
esa arquitectura.
---
Todos los agentes bajo este approach:
Take the current percept as input from the sensors and return an action to the actuators.

**Entrada:** Recibe una única percepción (percept) actual desde los sensores 
en cada paso de tiempo.

**Salida:** Devuelve una acción hacia los actuadores.

**Memoria interna (opcional):** El programa puede actualizar y mantener un estado
interno para recordar percepciones pasadas.

### Entre el concepto teórico (función de agente) y la implementación de software real 
La Función de Agente (El Concepto Matemático)
Es una función puramente abstracta. Describe el comportamiento ideal del agente.

### Definición matemática:  [ f: P^* --> A ]
Qué significa: Mapea el historial completo de todas las percepciones que 
el agente ha recibido en su vida (P^*) hacia una acción (A).

Limitación: Es una descripción externa.
No te dice cómo calcula la acción el agente
internamente, solo te dice cuál debería ser el resultado.

Puede requerir memoria o tiempo infinitos.

### El Programa de Agente (El Esqueleto en Código):
Es la implementación real en software que corre dentro de una máquina física 
 (la arquitectura).

* Firma del algoritmo: function AGENT(percept) returns action 
 
* Qué significa: Solo recibe una percepción a la vez (la actual). 
 Si el programa necesita recordar el pasado, el programador debe diseñar 
 una estructura de datos interna (como una lista o un estado) para guardarlo 
 de forma eficiente.
 
* Realidad: Debe lidiar con limitaciones de RAM, 
 almacenamiento y tiempo de procesador.



Comparacion resumida:

| Característica  | Función de Agente                  | Programa de Agente                                     |
|-----------------|------------------------------------|--------------------------------------------------------|
| Naturaleza      | Abstracta / Matemática             | Concreta / Código de software                          |
| Entrada directa | Todo el historial acumulado (P^*)  | Solo la percepción actual (`percept`)                  |
| Restricciones   | Ninguna (puede ser infinita)       | Limitada por la memoria y el procesador de la máquina  |

