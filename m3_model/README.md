# Evidencia 1: Sistemas multiagentes

## Interseccion con semaforo

Este modelo multiagente muestra el comportamiento de una interseccion entre dos calles
con un numero variable de carriles. La interseccion contiene un semaforo, el cual controla
el flujo de trafico a traves de la interseccion.

## Agentes involucrados

En total hay 3 diferentes tipos de agentes: un agente de carro, un agente de semaforo
y un agente de campo.

### Agente de campo

Este agente es el mas simple. Este únicamente consta de un campo que cambia de color periodicamente.

### Agente de semaforo

Este simula el funcionamiento de un semáforo real. Cada cierto tiempo, cambia de estado. Tiene tres estados:
rojo, amarillo y verde, cada uno con una duracion diferente.

### Agente de carro

Este es el agente más complejo. Cada carro tiene una direccion inicial, asi como una direccion hacia donde
quiere girar. El carro debe de cambiar de carril y cambiar su velocidad para
llegar a su destino. Un carro únicamente puede girar a la izquierda si se encuentra en el de hasta la
izquierda, e igualmente con la vuelta a la derecha. Un carro puede ir derecho en cualquier carril. No
pueden retornar. Los carros intentan siempre ir lo mas pronto posible hacia el carril
para realizar su giro deseado. Los carros siempre intentan ir a una velocidad de 1 bloque por tick.

## Interacciones entre agentes

Los carros no pueden chocar en esta simulacion, unicamente se detienen si se encuentran
con algun obstaculo. Si los carros se encuentran a menos de 5 celdas de distanca de la interseccion, estos
ven al semaforo que esta enfrente. Si esta en rojo, estos empiezan a frenar. Si esta en verde o amarillo,
estos continuan avanzando. Una vez lleguen a la interseccion y esten en su carril correcto, estos giraran.
En ese punto dejan de estar controlados por el semaforo anterior y le haran caso al semaforo del nuevo carril.
Igualmente, estos reciben una nueva direccion objetivo.

## Entorno

En si la simulacion consta de una cuadricula de N x N celdas. Las celdas centrales en X y Y son categorizadas como las
celdas del camino. El resto de las celdas se llenan de agentes de campo.

## Parametros de entrada

En si, la simulacion recibe un M numero de carriles para cada direccion. Igualmente, esta recibe un N de ancho y alto
para la cuadricula de la simulacion. Tambien tiene un porcentaje que representa la cantidad de carros que seran
insertados
por cada cuadro de la cuadricula.

## Proceso

La simulacion empieza calculando los limites de los caminos usando el numero de carriles y las dimensiones de la
cuadricula. Una vez definidos estos paremetros, se calcula la cantidad de carros por medio del porcentaje introducido
como
parametro. Es entonces cuando inicia la simulacion. En cada tick, cada carro calcula si deberia avanzar tomando en
cuenta
los otros carros, asi como su distancia al semaforo y su color. Igualmente, cada tick actualiza el estado del semaforo.
Una vez un carro gira, este recibe una nueva direccion objetivo. Finalmente, cuando el carro llega al borde de la 
cuadricula, este es movido al otro lado de la pantalla, con lo que continua dentro de la simulacion.

## Resultados
Esta simulacion modela un comportamiento aproximado al de los carros en una interseccion real. Sin embargo, se encuentra
limitada en varios aspectos claves. La mayor limitacion es la naturaleza discreta de usar una cuadricula. No hay cambios de
posicion lineales, que son esenciales para modelar el frenado de los carros y los efectos que estos tienen sobre el trafico.
Ademas, no se modelan valores de la mente humana como la agresividad y la compasion que tienen efectos marcados sobre
la manera en que los carros de mueven. Tambien se encuentra limitada por el hecho de que los carros unicamente se mueven
en 4 direcciones, lo limita la simulacion. 

---

[Repositorio](https://github.com/Stock44/M3-Actividad)


