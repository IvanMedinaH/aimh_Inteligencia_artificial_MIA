# Task environment:
The whole problem the agent faces

Its the world around the agent, as well as the rules surrounding it.

# Environment class
A category or collection of environment tasks that shares the same features
rules and structural properties.

we can see 7 types:

**Totalmente observable vs. Parcialmente observable:** 
Si los sensores del agente detectan todo el estado del entorno en 
cada momento (ej. ajedrez) o si hay información oculta 
(ej. póker o conducir).

**Agente único vs. Multiagente:** 
Si el agente opera solo (ej. un crucigrama) o si coexiste con otros agentes
que compiten o cooperan con él (ej. ajedrez).

**Determinista vs. Estocástico:** 
Si el siguiente estado del entorno está completamente determinado por
el estado actual y la acción del agente (ej. damas) o si existe incertidumbre .
y elementos al azar (ej. el clima o dados).

**Episódico vs. Secuencial:**
Si la experiencia del agente se divide en "episodios" independientes donde
las acciones pasadas no afectan al futuro (ej. clasificar imágenes) 
o si las decisiones actuales tienen consecuencias a 
largo plazo (ej. el ajedrez o la robótica).

**Estático vs. Dinámico:** 
Si el entorno permanece congelado mientras el agente delibera
(ej. crucigramas) o si cambia continuamente el mundo mientras el agente
piensa (ej. conducir un auto).

**Discreto vs. Continuo:** 
Si el entorno tiene un número finito y bien definido de estados 
y acciones (ej. el tablero de un juego) o si se basa en variables 
continuas como el tiempo, la velocidad o la distancia (ej. un robot móvil).

**Conocido vs. Desconocido:**
Esto se refiere al conocimiento del agente sobre las "leyes de la física" 
del entorno. Si es conocido, el agente sabe los resultados de s
us acciones (ej. un videojuego cuyas reglas ya están programadas). 
Si es desconocido, debe aprender cómo funciona mediante exploración.


**## Task environment dictates the level of complexity of the Agent's brain.**