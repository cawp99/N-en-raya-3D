## README

### Fase actual del proyecto: Implementación del juego 2D en consola

Hay varios archivos de Python en el repositorio. El juego 2D en consola lo estoy creando en el archivo `proyecto-en-consola.py`. Además tengo dos archivos auxiliares necesarios, `clases.py` y `funciones.py`, que contienen clases y funciones que estoy usando (respectivamente). Por ahora llevo esto implementado en el juego como tal:

#### Juego en consola

Es un programa de menú iterativo cuyo menú principal tiene opciones "Jugar" y "Salir", capaz de ignorar opciones no válidas y mostrar el menú principal de nuevo y de salir si se selecciona "Salir". Si se selecciona "Jugar", empieza un proceso que pide los nombres de los jugadores y el tamaño N del lado del tablero NxN, incluyendo manejo de excepciones tales como nombres vacíos, nombres repetidos, tamaños no enteros o tamaños no validos (menores o iguales a 2). Hasta ahora, estos valores se solicitan al usuario a través de un bucle, de manera que si ocurren excepciones se repite el procedimiento hasta que se introduzcan valores válidos, mostrando mensajes que indican la razón del error en cada caso.

Una vez que se crean los jugadores de manera satisfactoria, se crean dos instancias `jugador1` y `jugador2` de la clase `Jugador` definida en `clases.py`. También, una vez que se tiene el tamaño N guardado exitosamente, se muestra un "estatus" del juego antes de mostrar un menú secundario. Este estatus muestra los datos relevantes de los jugadores y las dimensiones del tablero. El menú secundario tiene opciones "Regresar" (al menú principal, siendo necesario repetir todo el proceso si se escoge "Jugar" de nuevo) e "Iniciar juego" (aún no implementado).

### Cosas en desarrollo

Hacer el juego como tal (xd), crearé las clases sugeridas por el enunciado y luego mostraré el estado en pantalla del tablero para que se pueda jugar con la consola introduciendo coordenadas. Ejemplo: si el usuario escribe "C4" entonces la casilla C4 se cambia al valor correspondiente dependiendo del turno del jugador que la seleccionó.

### Sobre las clases

#### Clase Jugador

Está robusta según mi opinión, además del método constructor y de métodos para mostrar y modificar los atributos, tiene los métodos `estado` que muestra un resumen de los atributos, `ganar_punto` que incrementa en 1 el puntaje y `cambiar_ficha` que alterna las fichas del jugador (esto se usaría entre cada ronda para que en la siguiente ronda se alternen fichas).
