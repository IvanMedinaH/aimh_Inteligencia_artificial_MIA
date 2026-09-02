    ** Sistema de recomendaciones de streaming **

Para poder diseñar un sistema de recomendaciones de streaming,
bajo el esquema PEAS, defino el siguiente concepto/prototipo:

### Programa software que:
    -Ofrece un mecanismo para definir perfiles
    -El perfil del usuario le permitira entender los gustos
    -Las recomendaciones se alinean basado en el perfil del usuario
    -El agente puede eventualmente ofrecer opciones alternativas
    -El agente puede navegar en Internet

| Letra | Significado | Pregunta guía                                                                                                                             |
| --- | --- |-------------------------------------------------------------------------------------------------------------------------------------------|
| **P** | *Performance* (medida de desempeño) | alineacion con los gustos, escala de valoracion, capacidad de adaptacion a nuevos gustos,                                                 |
| **E** | *Environment* (entorno) | online web, desktop app, mobile app                                                                                                       |
| **A** | *Actuators* (actuadores) | touch, teclado, pantalla, bocinas, microfonos                                                                                             |
| **S** | *Sensors* (sensores) | cuadros de input en pantalla, monitor del microfono, links, listas y demas controles en pantalla con los que el usuario puede interactuar |


## Environment Task:
**Parcialmente observable**:el asistente solo puede conocer lo que el usuario le permita 

**Secuencial**:El asistente ofrece basado en el perfil, y es ajustable, la alineacion
se puede medir con la escala de valoracion

**Dinamico**: el agente puede reaccionar al feedback y ofrecer mejores sugerencias

**Discreto/Continuo**: El agente puede ofrecer algo de forma aleatoria 
en tiempo(sin solicitud), si el usuario esta navegando su sistema, 
El agente reacciona en el momento en el que se solicita una recomendacion 

## Performance:
**(how to measure this system)**:

| Dimension a medir                 | Medido en                                                                                 |
|-----------------------------------|-------------------------------------------------------------------------------------------|
| alineado con el gusto del usuario | Escala de valoracion                                                                      |
| catalogo actualizado              | medicion en fechas de lanzamiento                                                         |
| calidad de streaming              | bitrate alto / kbps , resoluciones multiformato, multiples velocidades de conexion / mbps |