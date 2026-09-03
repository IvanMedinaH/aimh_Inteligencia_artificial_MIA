    ** Agente para asistencia en diagnostico medico **
Para poder diseñar un asistente en diagnostico medico,
bajo el esquema PEAS, pienso que es necesario entender
que caracteristicas puede/debe tener:

### Agente capaz de enteder sobre sintomas, patologias condiciones, :
    -valora las condiciones de llegada del paciente
    -Posee sensores de diferentes capacidades, niveles, y que trabajan a diferentes niveles de invasion
    -Puede llevar un estado del paciente a lo largo del tiempo
    -Posee acceso a una base de datos de conocimiento validado
    -Es capaz de sensar los signos vitales del paciente en tiempo real mediante tecnicas especificas
     
    

| Letra | Significado                          | Pregunta guía                                                                                                                                                                                              |
|-------|--------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **P** | *Performance* (medida de desempeño)  | -Eficacia de tratamiento / %, <br/>-Escala de recaida/% <br/>-eficacia de diagnostico(paciente no critico) /%, <br/>-Tiempo promedio de atencion/ minutos x paciente,<br/>- productividad financiera / $$$ |
| **E** | *Environment* (entorno)              | -El cuerpo fisico del paciente,                                                                                                                                                                            |
| **A** | *Actuators* (actuadores)             | -estetoscopio digital, pulsioximetro, baumanoemtro, termometro, analizador hematico, RX, tomografo, etc                                                                                                    |
| **S** | *Sensors* (sensores)                 | -Sensores especializados conectados a los dispositivos que el robot/agente puede escuchar activamente                                                                                                      |

## Task  Environment:
**Parcialmente observable:** 
El cuerpo humano es siempre parcialmente observable ya que se desconocen el estado de todos los sistemas al momento de la consulta
aunque tambien hay padecimientos que son observables en su totalidad, o que pueden considerarse sintomas o patologias, por lo que tambien puede ser observable bajo ciertas condiciones

**Episodico:** la evaluacion del agente es secuencial, pero la evaluacion de la evolucion puede ser episodica, y puede o no 
derivar en secuencias

**Dinamico:** el proceso de evaluacion  y cuidado es dinamico ya que no cambian al paciente solo por que el agente actue,
es el paciente quien toma accion posterior al diagnostico para poder cambiar su estado

**Continuidad:** -Distcreto para recetar , operar, medicar, diagnosticar, continuo para evaluar 

**Multi agent :** Multiagente para la revision, diagnostico de las diferentes dimensiones del paciente(pulsacion, ritmo cardiaco, oxigenacion)
un agente operando cada sistema, y evaluando independientemente

**determinismo:** el resultado puede ser estocastico, ya que 2 pacientes con biomarcadores y misma enfermedad pueden evolucionar diferente


## Performance:
**(how to measure this system)**:

| Dimension a medir                            | Medido en         |
|----------------------------------------------|-------------------|
| Eficacia de tratamiento                      | % de ganancia     |
| Escala de recaida                            | % de acierto      |
| eficacia de diagnostico(paciente no critico) | % acierto         |
| Tiempo promedio de atencion                  | min x paciente    |
| productividad financiera                     | $ mensual y anual |                              

  