# Informe Proyecto Lab. Algoritmos 1

## N en raya 3D

### Integrantes

* Jesús Isea carnet 16-10553  
* Carlos Wendehake carnet 16-11255

### Diseño

Este programa funciona a partir del programa en Python `proyecto-n-en-raya.py`. Se puede aplicar el análisis descendente de la siguiente manera:

1. Al iniciarse el programa, se carga la GUI hecha en `tkinter` y se abre el *menú inicial* (principal). En realidad la función `menu_inicial` es la única que se ejecuta por defecto al abrir la ventana principal.
2. El menú principal contiene dos botones con opciones *Iniciar Juego* y *Salir del Juego*, cada uno realiza lo que el nombre sugiere. El botón *Iniciar juego* tiene asociada la función `iniciar_juego` y el botón *Salir del juego* destruye la ventana principal a través de `tk.destroy()`. 
3. Si se ejecuta `iniciar_juego` se limpia la ventana principal (para ello definimos la función `reiniciar_ventana`) y se muestra un menú secundario para pedir los datos del juego. Este se ejecuta a través de la función `pedir_datos`.
4. El menú para pedir datos de nuevo limpia la ventana y a continuación muestra una pantalla donde a través de entries de tkinter y botones se pueden introducir los nombres de los dos jugadores y el lado del tablero, y dos botones adicionales: regresar e iniciar. Debido a la necesidad de que estas variables sean accesibles constantemente a lo largo de la ejecución del programa y ante la falta de alternativas, cuando se presiona *iniciar* se crean variables *globales* `nombre1`, `nombre2` y `tamaño` que almacenan el nombre del Jugador 1, del Jugador 2 y del lado N del tablero, respectivamente. Estos valores se almacenan con la función `guardar_datos`. El botón *regresar* nos devuelve al menú principal.
5. Además de guardar los datos, `guardar_datos` puede crear ventanas toplevel que muestran mensajes de error si (por ejemplo) el tamaño no cumple el tamaño mínimo N > 2. Si no hay errores, se ejecuta la función `empezar_juego`.
6. La función `empezar_juego` es la función que inicia el juego propiamente dicho. Tiene un argumento opcional `first` de tipo booleano, cuyo valor por defecto es *True*. Esto es para identificar y separar cuando se ejecuta el juego por primera vez o si es una ronda posterior. Si el juego se ejecuta por primera vez (es la primera ronda) pasa lo siguiente:
    1. Se crean dos instancias de la clase `Jugador` que serán los objetos que almacenan el nombre y puntaje de los Jugadores 1 y 2. El puntaje de ambos se inicializa como 0.
    2. Al jugador 1 se le asigna la ficha X, al jugador 2 se le asigna la ficha O.
7. Ya sea que se trate de la primera ronda o de una ronda posterior, `empezar_juego` crea a continuación una instancia de la clase `Tablero_3D`. La clase `Tablero_3D` almacena y modifica atributos como qué jugadores están jugando o el estado de cada casilla en las NxNxN posiciones. Además tiene métodos para poder actualizar una casilla específica además de métodos propios de la implementación del programa que ayudan a la visualización en la GUI, pero que no necesariamente afectan el juego per se.
8. Se reinicia la ventana principal y se imprimen los datos relevantes (nombre de jugadores, tipo de ficha, puntaje) a través de la función `datos_tablero`, que los muestra en un frame a través de labels en la GUI. Debajo de esta información se muestra un tablero de nivel NxN consistente de botones que se pueden hacer clic y que representan las casillas del tablero. Cada casilla, si ha sido seleccionada previamente, tiene un color más oscuro y el texto cambia de manera acorde a la selección del jugador correspondiente. Esto se logra con la función `imprimir_tablero`, que tiene un argumento `n` entero que representa el nivel del tablero. La función `imprimir_tablero` también muestra con un label el nivel del tablero actual y hay dos botones que permiten subir y bajar de nivel (de esa manera se pueden acceder a todos los N tableros de nivel). 
9. Los botones de subir y bajar nivel tienen asociadas a las funciones `subir_nivel` y `bajar_nivel`, respectivamente. Estas funciones limpian el frame donde se imprime el tablero y también llaman a `imprimir_tablero` con el argumento del nivel correspondiente. En los casos borde, los botones de subir y bajar se pueden seguir haciendo click pero al hacerlo no sucede nada.
10. En este punto sucede el juego. La interacción de usuario consiste en usar los botones de subir y bajar nivel para desplazarse al tablero de nivel que deseen. En cualquier tablero de nivel pueden seleccionar una de las casillas que esté libre (si seleccionan una que esté ocupada, se crea una ventana toplevel de error y no da por terminado el turno). Las casillas (botones) tienen asociada la función `casilla_presionada`. Al hacer esto, pueden suceder dos cosas (además del mensaje de error):
    * Si el juego llega a un estado de finalización (empate o victoria para el jugador que acaba de jugar), se muestra una ventana toplevel que indica el resultado de la ronda y tiene las opciones *continuar* para crear una nueva ronda y *menú principal*, para ir al menú principal. Ambas opciones destruyen la ventana toplevel. También se limpia la ventana principal mientras no se haya presionado alguno de los botones de la ventana toplevel, para evitar que se sigan seleccionando casillas cuando en realidad ya la ronda está terminada.
    * Si el juego no llega a un estado de finalización, a través de la función `actualizar_datos` (que se ejecuta cada 100 ms a menos que se limpie la ventana principal), se actualiza el label que indica quién tiene el turno, y se utiliza el método `siguiente_turno()` de la clase `Tablero_3D` para indicarle al tablero que ahora juega el otro jugador. La ficha mostrada al seleccionar una casilla también se cambia de manera acorde.  
    * Ambos escenarios (incluyendo el mensaje de error cuando se selecciona una casilla ya ocupada) están contemplados dentro de `casilla_presionada`.

11. La función `casilla_presionada` extrae las coordenadas de la casilla (incluyendo el nivel) a través de una variable de control de tipo *IntVar* llamada `variable_nivel`, que se corresponde con el nivel del tablero mostrado actualmente. La fila y columna de la casilla se extraen a través del método `grid_info` (las casillas se ponen en el frame del tablero a través del método `grid`).
12. Usando estas coordenadas, se verifica el atributo `estado` del objeto de tablero de la clase `Tablero_3D`, que no es más que una hipermatriz NxNxN de objetos de la clase `Casilla`. Cada una de estas casillas tiene un atributo llamado `estado` que refleja si está vacía, si es del jugador de las X o del jugador de las O. Si la casilla seleccionada tiene un estado no-vacío se muestra una ventana toplevel de error. En caso contrario, a través del método `actualizar_casilla` de la clase `Tablero_3D` se modifica el estado de la casilla para que refleje el Jugador que la acaba de seleccionar.
13. En la GUI, cuando una casilla acaba de ser actualizada, se cambia el color de fondo y el color del texto, además que se muestra una "X" o una "O", respectivamente. Esto se mantiene incluso aunque se mueva de nivel para mostrar los distintos tableros (`imprimir_tablero` en realidad imprime el tablero tal como está almacenado al momento de ejecutarse, el valor inicial de todas las casillas como vacías forma parte de la instanciación a la hora de crear el objeto de `Tablero_3D`).
14. Inmediatamente después de esto, se ejecuta la función `verificar_ganador`, para identificar si tras la jugada que acaba de hacerse se llega a un estado de finalización. Esta función llama a la función `hay_ganador` del módulo `verificaciones.py`. En esencia, `verificar_ganador` verifica si alguna de las líneas permitidas como ganadoras tiene elementos de la misma clase (misma ficha o vacíos). Si son vacíos se ignora, pero si encuentra lineas del mismo tipo entonces abre una ventana toplevel con el resultado de la ronda con los botones *continuar* y *menú principal*. La función `hay_ganador` es ingeniosa porque en vez de verificar manualmente las filas intertablero (excepto las intertablero puras de una misma posición, que se verifican manualmente en la función con un bucle), verifica las filas en una "matriz de proyección" que es como la sombra que arrojan las fichas sobre los distintos niveles en un "nivel de suelo". Si en la sombra del suelo se forman líneas conectadas del mismo tipo, es porque hay líneas completas repartidas de alguna manera entre los tableros. Si no se encuentra un ganador inmediato, también cuenta la cantidad de movimientos legales restantes (para identificar empates).
15. Al presionar la opción *continuar* en la ventana toplevel que sale al finalizar la ronda, se ejecuta la función `continuar`, que intercambia los nombres `Jugador1` y `Jugador2` (para que se alternen fichas), y llama a `empezar_juego` con el argumento `first = False` (así no se crean nuevas instancias de Jugador sino que se mantienen, lo que es necesario para mantener los puntajes).
16. El proceso continúa hasta que se cierra la ventana principal o se devuelve al menú principal para salir del juego.

### Estructuras de datos

Como se vio pues, las clases que se definen en el proyecto son las siguientes, almacenadas en `clases.py`:
* `Jugador`, cuyos atributos son `nombre` y `puntaje`
* `Casilla`, cuyo atributo `estado` almacena si está vacía (0), una X (1) o un O (2).
* `Tablero_3D`. La docstring de esta clase es:
>Una clase que contiene el tablero 3D y la información necesaria para llevar a cabo el juego.
>
> ### Atributos
>   * `lado`: Un entero N > 2 que representa el lado.
>   * `estado`: Una matriz NxNxN de objetos de la clase 'Casilla', que representa
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
>   * `matriz_numerica`: Matrix NxNxN de N=`lado` que contiene los valores de estado de cada casilla en la posición
>   [nivel][i][j].
>   * `matriz_proyeccion`: Retorna una matriz numérica NxN de lado N=`lado` que contiene
>   en la entrada [i][j] el valor de `estado` de la Casilla de posición [i][j] de
>   `estado` del tablero. En otras palabras, `matriz_proyeccion` retorna una matriz de enteros
>   0, 1 y 2. Habrá un estado especial: 3, que representa que hay tanto X como O en esa casilla a
>   la hora de hacer la proyección.
>   * `actualizar_casilla`: Dependiendo de quién es el turno, recibe las coordenadas
>   correspondientes a una casilla y la actualiza para representar quién la modificó
>   * `movimientos_restantes`: Retorna un entero correspondiente a la cantidad de movimientos
>   legales que quedan en el tablero (hasta 0, que significa que no hay más)

### Subproblemas clave del proyecto

1. Implementación de la GUI, imprimir los tableros de nivel, desplazarse entre niveles, mostrar el estado de las casillas en los botones y que se actualicen, limpiar la ventana o los frames cuando sea necesario.
2. Crear estructuras de datos apropiadas para almacenar el nombre y puntaje de los Jugadores, el turno actual y el estado de las casillas, además de permitir actualizar el estado de éstas.
3. Implementar las verificaciones de condiciones de victoria.
4. Crear una cantidad indeterminada de rondas de manera sucesiva, intercambiando fichas y manteniendo los puntajes de cada jugador.

### Estado actual del proyecto

Es funcional, aunque se sospecha que si el lado del tablero es demasiado grande puede ser que no quepa en pantalla (o que ponga demasiado lenta la computadora).

### Conclusiones

Lo más importante de este proyecto es la familiarización con las interfaces gráficas de python y tkinter además de una introducción no-oficial a la programación orientada a objetos que puede ser útil en el siguiente curso de algoritmos II.

Se recomienda no introducir valores muy grandes de lado para el tablero, realmente se vuelve muy impráctico de jugar incluso con valores pequeños de N como 4 ó 5.

### Bibliografía

* Documentación oficial de Python
* Videos de YouTube:
    * Curso de tkinter: https://www.youtube.com/playlist?list=PL7HAy5R0ehQXb2aFKOKyeCMequxyb5jzJ
    * POO en Python: https://www.youtube.com/watch?v=JVNirg9qs4M&ab_channel=BitBoss
    * StackOverflow: https://stackoverflow.com/