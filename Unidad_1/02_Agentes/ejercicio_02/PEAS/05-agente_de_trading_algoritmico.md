    ** Agente de Trading Algoritmico **
Para poder diseñar un agente de Trading Algoritmico,
bajo el esquema PEAS, pienso que es necesario entender que caracteristicas tiene:

### Agente capaz de enteder los mercados locales e interacionales para:
    -Ejecutar ordenes de compra
    -Ejecutar ordenes de venta
    -Ejecutar analisis tecnico
    -Poder presentar graficas 
    -Reconocimiento de patrones
    -Poder conectar y consumir APIs
    

| Letra | Significado | Pregunta guía                                                                                                                        |
| --- | --- |--------------------------------------------------------------------------------------------------------------------------------------|
| **P** | *Performance* (medida de desempeño)| Desempeño en compras /% de ganancia <br/>-Exactidud de predicciones /% de acertitud, ROI / %anual                                    |
| **E** | *Environment* (entorno) | medio digital /desktop, web, movil app                                                                                               |
| **A** | *Actuators* (actuadores) | APIs de Mercados, Sitios de noticias, Otros agentes                                                                                  |
| **S** | *Sensors* (sensores) | APIS de Mercados, APIS de Banca central, scripts personalizados y algoritmos que monitoreen empresas, noticias, y otras aplicaciones |

## Task  Environment:
**Parcialmente observable:** dada la volatilidad de los mercados, solo se puede ir conociendo el estado parcial de estos 

**Episodico:** cada operacion es independiente de la anterior

**Dinamico:** El mercado evoluciona continuamente, por lo tanto es dinamico a lo largo del dia

**Continuo:** Las magnitudes de los cambios en los valores de las acciones pueden ser muy pequeñas o muy grandes 

**Multi agent :** el sistema es multi agentico, ya que se necesitan tomar multiples decisiones en tiempo real para el mejor aprovechamiento  

**determinismo:** Estocastico, cualquier accion efectuada por el agente puede variar en resultado, dada la naturaleza de los mercados,
pero tambien dada la magnitud de operaciones, y gracias la ley de grandes numeros puede analizar volumenes grandes de datos y obtener resultados
deterministicos.
*Nota antes habia visto este video (https://www.youtube.com/watch?v=KZeIEiBrT_w&t=277s)

## Performance:
**(how to measure this system)**:

| Dimension a medir         | Medido en             |
|---------------------------|-----------------------|
| Desempeño en compras      | /% de ganancia        |
| Exactidud de predicciones | /% de acierto         |
| ROI(retorno de inversion) | %anual                |
| Perdidas maxima esperada  | valores de tolerancia |
|                           |                       |                              