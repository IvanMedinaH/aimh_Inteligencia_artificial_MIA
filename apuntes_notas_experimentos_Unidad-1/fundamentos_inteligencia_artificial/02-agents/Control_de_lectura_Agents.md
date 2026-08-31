# Agents

An **_agent_**  is an entity that perceives its environment
through sensors and act upon it using its actuators
to achieve its goals.


- **_sensors_**
    anything that can help the agent to get in contact with the world/environment

- **_environment_**
    the universe defined around the agent, defined by certain characteristics

- **_actuators_**
    the means used by the agent to act upon the environment, 
    defined by specific actions
    
- **_percept_**:
    content an agent's sensor is perceiving
- **_percept sequence_**:
    complete history of of everything the agent has perceived

"An agent **CAN NOT** react to anything it _does not know_ or have perceived."

Fundamentally classified in 5 types(external information):

    - Reactivos simples
    - Reactivos basados en modelos
    - Basados en objetivos
    - Basados en utilidad 
    - Agentes de aprendizaje.

The book (AIMA) classified agents in :
    - simple reflex
    - model-based reflex
    - goal-based agents 
    -utility-based agents

# Design principles (Intelligent)
is a rational agent if have:
1. [x] Performance meassure
2. [x] Prior knowledge of the environment
3. [x] Actions can be performed
4. [x] percept sequence to date 


What is a rational Agent?
if under each percept sequence, the agent select an action, that is expected to maximize its performance meassure
given the evidence provided by the percept sequence and whatever built in knowledge the agent has

Given an environment an agent can be performant or not, depending on the Performance measure
Environment can be known, but not the distribution, ammount, periodicity or probability of the 
location of the elements where the agent has to act

there is a limited set of actions 

a correct perception of location, periodicity, distribution, etc of the agent depends of the 
architecture of the agent

Agents can have critical dimensions where to act and be measured as rational
critical dimensions:
percepted elements as "dimensions"in where the agent
is evaluated for correctness upon is acting
over the environment. 

* cognitive & learning
  * autonomy degree
  * adaptability
  * explainability
  
* Social & interactive
  * Alignment
  * colaboration
  * Communication
  
* operational  & execution 
  * latency (speed of the perceive-plan-act loop)
  * resource constraints(computational footprint, memory usage, and energy consumption)
  * durable memory(depth of information retention.)
  
* Systemic & Architectural 
  * groundedness
  * composisionality
  * granularity of control
  
* Risk & Security
  * robustness resillience
  * Exploration vs. Exploitation(of knowledge gathered / gathering new knowledge)
  * fallback strategy (things can go wrong, what next?)
  
* Self-Awareness & Metacognitive
  * metacognition (Self-Monitoring)
  * statefulness (persistent awareness of the agent's own identity)
  
Y AUNQUE TODOS ESAS DIMENSIONES PUEDAN OCURRIR Y SERVIR PARA EVALUAR A UN AGENTE
NO PUEDE OCURRIR EN RETROSPECTIVA

### **<<you only know what the best choice was after everything has already happened<<**

------------------

**Omniscience (Impossible):** Knowing the actual outcome of an action before it happens. 
This requires an impossible, perfect perception of the future and every 
hidden variable in the environment.

**Rationality (Achievable):** Doing the expected best action based on the
information available and the percepts received up to that point.