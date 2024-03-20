## README

### Fase actual del proyecto: Implementación del juego 2D en consola

Hay varios archivos de Python en el repositorio. El juego 2D en consola lo estoy creando en el archivo `proyecto-en-consola.py`. Además tengo dos archivos auxiliares necesarios, `clases.py` y `funciones.py`, que contienen clases y funciones que estoy usando (respectivamente). Por ahora llevo esto implementado en el juego como tal:

#### Juego en consola

Es un programa de menú iterativo cuyo menú principal tiene opciones "Jugar" y "Salir", capaz de ignorar opciones no válidas y mostrar el menú principal de nuevo y de salir si se selecciona "Salir". Si se selecciona "Jugar", empieza un proceso que pide los nombres de los jugadores y el tamaño N del lado del tablero NxN, incluyendo manejo de excepciones tales como nombres vacíos, nombres repetidos, tamaños no enteros o tamaños no validos (menores o iguales a 2). Hasta ahora, estos valores se solicitan al usuario a través de un bucle, de manera que si ocurren excepciones se repite el procedimiento hasta que se introduzcan valores válidos, mostrando mensajes que indican la razón del error en cada caso.

Una vez que se crean los jugadores de manera satisfactoria, se crean dos instancias `jugador1` y `jugador2` de la clase `Jugador` definida en `clases.py`. También, una vez que se tiene el tamaño N guardado exitosamente, se muestra un "estatus" del juego antes de mostrar un menú secundario. Este estatus muestra los datos relevantes de los jugadores y las dimensiones del tablero. El menú secundario tiene opciones "Regresar" (al menú principal, siendo necesario repetir todo el proceso si se escoge "Jugar" de nuevo) e "Iniciar juego".

Al seleccionar "Iniciar juego", se muestran los datos esenciales (nombre de los jugadores, puntaje, quién tiene el turno) y además se muestra una grilla
correspondiente a la versión 2D del tablero, con valores para las casillas "-" por inicializarse vacías. En los bordes de la grilla se muestran coordenadas
para que los usuarios sepan qué casilla modificar

### Cosas en desarrollo

Estoy trabajando en la jugabilidad de las rondas, que los usuarios puedan seleccionar casillas y que se modifiquen apropiadamente. Después de eso implementaré
alguna manera para que se verifiquen los estados de finalización de una ronda (lineas), que se aumente el punto correspondientemente y que se inicie una nueva.

**Importante:** A diferencia de otras partes del código, como el resultado que nos piden es en interfaz gráfica y no en consola, esta parte del código
no estará tan blindada con manejo de excepciones y consideraciones estéticas, es más para probar las funciones de verificación y de manejo de las
rondas.

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




