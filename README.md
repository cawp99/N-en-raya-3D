## README

### Fase actual del proyecto: Juego 2D en consola LISTA

Hay varios archivos de Python en el repositorio. El juego 2D en consola lo estoy creando en el archivo `proyecto-en-consola.py`. Además tengo dos archivos auxiliares necesarios, `clases.py` y `funciones.py`, que contienen clases y funciones que estoy usando (respectivamente). Por ahora llevo esto implementado en el juego como tal:

#### Juego en consola

Es un programa de menú iterativo cuyo menú principal tiene opciones "Jugar" y "Salir", capaz de ignorar opciones no válidas y mostrar el menú principal de nuevo y de salir si se selecciona "Salir". Si se selecciona "Jugar", empieza un proceso que pide los nombres de los jugadores y el tamaño N del lado del tablero NxN, incluyendo manejo de excepciones tales como nombres vacíos, nombres repetidos, tamaños no enteros o tamaños no validos (menores o iguales a 2). Hasta ahora, estos valores se solicitan al usuario a través de un bucle, de manera que si ocurren excepciones se repite el procedimiento hasta que se introduzcan valores válidos, mostrando mensajes que indican la razón del error en cada caso.

Una vez que se crean los jugadores de manera satisfactoria, se crean dos instancias `jugador1` y `jugador2` de la clase `Jugador` definida en `clases.py`. También, una vez que se tiene el tamaño N guardado exitosamente, se muestra un "estatus" del juego antes de mostrar un menú secundario. Este estatus muestra los datos relevantes de los jugadores y las dimensiones del tablero. El menú secundario tiene opciones "Regresar" (al menú principal, siendo necesario repetir todo el proceso si se escoge "Jugar" de nuevo) e "Iniciar juego".

Al seleccionar "Iniciar juego", se muestran los datos esenciales (nombre de los jugadores, puntaje, quién tiene el turno) y además se muestra una grilla
correspondiente a la versión 2D del tablero, con valores para las casillas "-" por inicializarse vacías. En los bordes de la grilla se muestran coordenadas
para que los usuarios sepan qué casilla modificar.

La entrada de casillas para modificar es a través de coordenadas (X,Y) horizontal y luego vertical como se muestran en la grilla que sale cuando se imprime el tablero. El juego ya es capaz de detectar cuando un jugador gana la ronda, además de poder
ir cambiando turno por turno para mostrar el nombre cuando se imprime el estado del juego y modificar las casillas con la ficha correspondiente.

Ya se puede jugar varias rondas después de haber terminado una ronda y gracias a intercambiar
los argumentos posicionales a la hora de llamar a la función `jugar``y al método `ganar_punto` de la clase Jugador, se almacenan los puntajes entre ronda.

### Notas

**Importante:** A diferencia de otras partes del código, la parte de imprimir el tablero en consola y de introducir las coordenadas con la entrada estándar, como el resultado que nos piden es en interfaz gráfica y no en consola, esta parte del código no estará tan blindada con manejo de excepciones y consideraciones estéticas, es más para probar las funciones de verificación y de manejo de las rondas. *Asumimos que los desarrolladores que lo ejecuten como parte de esta etapa preliminar intentarán no buscar excepciones intencionalmente...* ;)

### En desarrollo 

¡Terminé la parte de consola!

### Sugerencias para la interfaz gráfica

Las clases funcionan de manera independiente a cómo se imprimen y cómo se modifican las casillas. Supongo que cuando empieces a trabajar con tkinter, se me ocurre que una vez se 
soliciten los datos de jugadores se creen las instancias de Jugador respectivas y 
para jugar, esa función puede generar un arreglo dentro un frame de botones que al hacer
click se pongan como la ficha correspondiente, pero que tambien vayan modificando el tablero con el método `actualizar_casilla` de la clase Tablero_2D porque es la que lleva el juego.

### Sobre las clases

#### Clase Jugador

Está robusta según mi opinión, además del método constructor y de métodos para mostrar y modificar los atributos, tiene los métodos `estado` que muestra un resumen de los atributos, `ganar_punto` que incrementa en 1 el puntaje y `cambiar_ficha` que alterna las fichas del jugador (esto se usaría entre cada ronda para que en la siguiente ronda se alternen fichas).

#### Clase Casilla

Su único atributo es su `estado`, puede ser 0 si está vacía, 1 si es "X" o 2 si es "O". Además tiene el método `actualizar` que permite cambiar su estado
dependiendo del jugador que tiene el turno.

#### Clase Tablero_2D

Representa el estado del tablero de un juego en dos dimensiones. Aquí está su docstring:
>Una clase que contiene el tablero 2D, el turno actual y el estado del juego hasta el momento, además de los estados de finalización.
>   ### Atributos
>   * `lado`: Un entero N > 2 que representa el lado.
>   * `estado`: Una matriz NxN de objetos de la clase 'Casilla', que representa
>   el estado actual del tablero
>   * `jugadores`: Una lista de dos entradas que son de la clase 'Jugador' que representa
>   quienes están jugando el juego
>   * `turno`: Un entero que representa de qué jugador es el turno (1, 2)
>   * `ganador`: Un entero que representa si el juego está inconcluso (0), o quién es el
>   ganador del juego (1, 2, 3). El valor 3 representa un empate.
>
>   ### Métodos
>   * Un método constructor
>   * `siguiente_turno`: Le da el turno al otro jugador, `turno` se modifica apropiadamente.
>   * `matriz_numerica`: Retorna una matriz numérica NxN de lado N=`lado` que contiene
>   en la entrada [i][j] el valor de `estado` de la Casilla de posición [i][j] de
>   `estado` del tablero. En otras palabras, `matriz_numerica` retorna una matriz de enteros
>   0, 1 y 2.
>   * `actualizar_casilla`: Dependiendo de quién es el turno, recibe las coordenadas
>   correspondientes a una casilla y la actualiza para representar quién la modificó
>   * `movimientos_restantes`: Retorna un entero correspondiente a la cantidad de movimientos
>   legales que quedan en el tablero (hasta 0, que significa que no hay más)
