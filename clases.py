#Un archivo que contiene las clases necesarias para el proyecto
from typing import List
import copy

class Jugador():
    """Una clase que almacene el Jugador, nombre, puntaje y que tipo de ficha juega.

    ### Atributos
    * `nombre`: Una string no vacía, el nombre del jugador
    * `ficha_actual`: Una string no vacía con dos valores: "X", "O". Representa
    el tipo de ficha que juega el jugador en cada partida.
    * `puntaje`: Un entero no negativo que representa la cantidad de partidas
    ganadas de este jugador.

    ### Métodos
    * Un método constructor
    * `estado`: Imprime el estado actual del Jugador incluyendo todos sus atributos.
    * `ganar_punto`: Aumenta el valor de `puntaje` por 1.
    * `cambiar_ficha`: Cambia el valor de `ficha_actual` por el otro valor ("X" <-> "O")
    """

    def __init__(self, nombre:str, ficha_actual:str)->'Jugador':
        """Crea instancias de Jugador.
        
        ### Argumentos
        * `nombre`: Una string
        * `ficha_actual`: Una string "X" ó "O"

        ### Retorno
        Una instancia de Jugador con los atributos asignados por los parámetros nombre y 
        ficha_actual. El atributo puntaje = 0.

        ### Excepciones
        * Si `nombre` es vacío, lanza ValueError.
        * Si `ficha_actual` es distinta a "X" ó "O" lanza ValueError.

        ### Otros
        Este método tambien inicializa el atributo `puntaje` a un valor por defecto de 0.
        """

        if len(nombre) == 0:
            raise ValueError("El nombre de un jugador no puede ser vacío.")
        
        if ficha_actual not in ["X", "O"]:
            raise ValueError("La ficha no es un válida")
        
        self.puntaje : int = 0
        self.nombre :str = nombre
        self.ficha_actual : str = ficha_actual

    def estado(self)->None:
        """Muestra en la salida estándar los atributos de un Jugador."""

        print(f"Nombre: {self.nombre}")
        print(f"Ficha actual: {self.ficha_actual}")
        print(f"Puntaje actual: {self.puntaje}")

    
    def ganar_punto(self):
        """Incrementa `puntaje` en 1 unidad."""

        self.puntaje = self.puntaje + 1

    def cambiar_ficha(self):
        """Alterna el valor de `ficha_actual` por el otro en ["X", "O"]"""

        if self.ficha_actual == "X":
            self.ficha_actual = "O"
        else:
            self.ficha_actual = "X"

class Casilla():
    """Una clase que almacene las casillas, su estado (vacío, X, O) y
    los métodos relevantes para ella dentro del juego.

    ### Atributos
    * `estado`: Un valor entero (0, 1, 2) que representa si la casilla
    está vacía (0) tiene una X (1) o un O (2).

    ### Métodos
    * Un método constructor
    * `actualizar`: Cambiar el estado de al estado correspondiente al del jugador
    respectivo, pero de acuerdo a cuál jugador tenga el turno.
    """

    def __init__(self)->'Casilla':
        """Crea una instancia de casilla, por defecto estándo vacía."""

        self.estado = 0

    
    def set_estado(self, estado:int):
        """Modifica el estado de la casilla.
        
        ###Excepciones
        Si el argumento no es entero lanza TypeError. Si es distinto a 0, 1, 2 entonces
        lanza ValueError.
        """

        try:
            estado = int(estado)
        except:
            raise TypeError("El estado debe ser entero")
        
        if estado not in [0, 1, 2]:
            raise ValueError("El estado no es válido")
        
        self.estado = estado

    def actualizar(self, turno:int):
        """Cambia el estado de la casilla al estado correspondiente al del jugador
        que la seleccione en su turno.
        
        El argumento `turno` vale 1 ó 2, indicando quien juega.
        
        Al ejecutar este metodo, el atributo `estado` vale 1 ó 2, respectivamente
        igual a `turno`."""
        #por hacer
        if turno == 1:
            self.estado = 1
        else:
            self.estado = 2

class Tablero_2D():
    """Una clase que contiene el tablero 2D, el turno actual y el estado del juego hasta
    el momento, además de los estados de finalización.
    
    ### Atributos
    * `lado`: Un entero N > 2 que representa el lado.
    * `estado`: Una matriz NxN de objetos de la clase 'Casilla', que representa
    el estado actual del tablero
    * `jugadores`: Una lista de dos entradas que son de la clase 'Jugador' que representa
    quienes están jugando el juego
    * `turno`: Un entero que representa de qué jugador es el turno (1, 2)
    * `ganador`: Un entero que representa si el juego está inconcluso (0), o quién es el
    ganador del juego (1, 2, 3). El valor 3 representa un empate.


    ### Métodos
    * Un método constructor
    * `siguiente_turno`: Le da el turno al otro jugador, `turno` se modifica apropiadamente.
    * `matriz_numerica`: Retorna una matriz numérica NxN de lado N=`lado` que contiene
    en la entrada [i][j] el valor de `estado` de la Casilla de posición [i][j] de
    `estado` del tablero. En otras palabras, `matriz_numerica` retorna una matriz de enteros
    0, 1 y 2.
    * `actualizar_casilla`: Dependiendo de quién es el turno, recibe las coordenadas
    correspondientes a una casilla y la actualiza para representar quién la modificó
    * `movimientos_restantes`: Retorna un entero correspondiente a la cantidad de movimientos
    legales que quedan en el tablero (hasta 0, que significa que no hay más)
    """

    def __init__(self, jugador1:'Jugador', jugador2:'Jugador', lado:int)->'Tablero_2D':
        """Crea una instancia de Tablero_2D.
        
        ### Parámetros
        * `jugador1`: Un objeto de la clase Jugador
        * `jugador2`: Un objeto de la clase Jugador
        * `lado`: Un entero N > 2

        ### Excepciones
        * Si `lado` <= 2 arroja ValueError.

        ### Retorno
        El tablero se inicializa con los atributos:
        * `lado` igual al argumento `lado`
        * `estado` igual a una matriz `lado`x`lado` de Casillas vacías
        * `jugadores` consistiendo en una lista formada por [jugador1, jugador2]
        * `turno` igual a 1 (Jugador 1 va primero en la primera ronda)
        """

        try:
            lado = int(lado)
        except:
            raise TypeError("lado no es entero")
        
        if lado <= 2:
            raise ValueError("El lado debe ser N > 2")
        
        self.lado : int = lado
        
        estado : List[List['Casilla']] = []
        fila : List['Casilla'] = [] 
        for i in range(lado):
            fila = []
            for j in range(lado):
                fila.append(Casilla())

            estado.append(fila)
        
        self.estado : List[List['Casilla']] = estado

        self.jugadores : List['Jugador'] = [jugador1, jugador2]

        self.turno : int = 1


    def siguiente_turno(self):
        """Un método para indicar que el turno es del próximo jugador ahora."""
        if self.turno == 1:
            self.turno = 2
        else:
            self.turno = 1

    def matriz_numerica(self)->List[List[int]]:
        """Un método que devuelve la matriz numérica de estados asociados a cada casilla
    del tablero.
    
    ### Retorno
    List[List[int]]: Una matriz NxN de lado N = lado del tablero que contiene
    en la entrada [i][j] el valor de `estado` de la Casilla de posición [i][j] de
    `estado` del tablero. En otras palabras, `matriz_numerica` retorna una matriz de enteros
    0, 1 y 2.
        """

        matriz:List[List[int]]=[]
        fila:List[int]=[]
        for i in range(self.lado):
            fila=[]
            for j in range(self.lado):
                fila.append(getattr(self.estado[i][j], "estado"))
            
            matriz.append(fila)

        return matriz

    def actualizar_casilla(self, fila:int, columna:int):
        """Un método para actualizar el valor de una casilla,
        dependiendo de quién sea el jugador con el turno
        que la seleccione
        
        ### Argumentos
        * `fila`: Un número de fila válido en la matriz que representa el tablero
        * `columna`: Un número de columna válido en la matriz que representa el tablero

        ### Ejecución
        Accede a la casilla de posición [i][j] en el estado del tablero y modifica su
        atributo estado para que refleje el jugador que la acaba de seleccionar.
        """

        casilla:'Casilla' = self.estado[fila][columna]
        if getattr(casilla, "estado") == 0: #está vacía, movimiento legal
            casilla.actualizar(self.turno)
        else: #no vacía
            raise ValueError("No se puede modificar una casilla no vacía")
        
    def movimientos_restantes(self)->int:
        """Un método que retorna la cantidad de movimientos restantes posibles
        a partir de la posición actual del tablero.
        
        ### Retorno
        int: La cantidad de casillas vacías en el tablero."""

        matriz:List[List[int]]=self.matriz_numerica()
        lado:int = self.lado

        suma:int = 0
        for i in range(lado):
            for j in range(lado):
                if matriz[i][j] == 0:
                    suma = suma + 1

        return suma

class Tablero_3D(Tablero_2D):
    """
    Una clase que contiene el tablero 3D y la información necesaria para llevar a cabo el juego.

    ### Atributos
    * `lado`: Un entero N > 2 que representa el lado.
    * `estado`: Una matriz NxNxN de objetos de la clase 'Casilla', que representa
    el estado actual del tablero
    * `jugadores`: Una lista de dos entradas que son de la clase 'Jugador' que representa
    quienes están jugando el juego
    * `turno`: Un entero que representa de qué jugador es el turno (1, 2)
    * `ganador`: Un entero que representa si el juego está inconcluso (0), o quién es el
    ganador del juego (1, 2, 3). El valor 3 representa un empate.


    ### Métodos
    * Un método constructor
    * `siguiente_turno`: Le da el turno al otro jugador, `turno` se modifica apropiadamente.
    * `matriz_numerica`: Matrix NxNxN de N=`lado` que contiene los valores de estado de cada casilla en la posición
    [nivel][i][j].
    * `matriz_proyeccion`: Retorna una matriz numérica NxN de lado N=`lado` que contiene
    en la entrada [i][j] el valor de `estado` de la Casilla de posición [i][j] de
    `estado` del tablero. En otras palabras, `matriz_proyeccion` retorna una matriz de enteros
    0, 1 y 2. Habrá un estado especial: 3, que representa que hay tanto X como O en esa casilla a
    la hora de hacer la proyección.
    * `actualizar_casilla`: Dependiendo de quién es el turno, recibe las coordenadas
    correspondientes a una casilla y la actualiza para representar quién la modificó
    * `movimientos_restantes`: Retorna un entero correspondiente a la cantidad de movimientos
    legales que quedan en el tablero (hasta 0, que significa que no hay más)    
    """

    def __init__(self, jugador1:'Jugador', jugador2:'Jugador', lado:int)->'Tablero_3D':
        """Crea una instancia de Tablero_3D.
        
        ### Parámetros
        * `jugador1`: Un objeto de la clase Jugador
        * `jugador2`: Un objeto de la clase Jugador
        * `lado`: Un entero N > 2

        ### Excepciones
        * Si `lado` <= 2 arroja ValueError.

        ### Retorno
        El tablero se inicializa con los atributos:
        * `lado` igual al argumento `lado`
        * `estado` igual a una matriz `lado`x`lado` de Casillas vacías
        * `jugadores` consistiendo en una lista formada por [jugador1, jugador2]
        * `turno` igual a 1 (Jugador 1 va primero en la primera ronda)
        """

        try:
            lado = int(lado)
        except:
            raise TypeError("lado no es entero")
        
        if lado <= 2:
            raise ValueError("El lado debe ser N > 2")
        
        self.lado : int = lado
        
        estado : List[List[List['Casilla']]] = []
        subtablero : List[List['Casilla']] = []
        fila : List['Casilla'] = [] 
        for i in range(lado):
            subtablero = []
            for j in range(lado):
                fila = []
                for k in range(lado):
                    fila.append(Casilla())

                subtablero.append(fila)

            estado.append(subtablero)
        
        self.estado : List[List[List['Casilla']]] = estado

        self.jugadores : List['Jugador'] = [jugador1, jugador2]

        self.turno : int = 1

    def matriz_proyeccion(self)-> List[List[int]]:
        """Un método que devuelve la matriz numérica de estados asociados a cada casilla
    del tablero, proyectada a un mismo nivel.
    
    ### Retorno
    List[List[int]]: Una matriz NxN de lado N = lado del tablero que contiene
    en la entrada [i][j] el valor de `estado` de la Casilla de posición [i][j] de
    `estado` del tablero en cada nivel. En otras palabras, `matriz_pryeccion` retorna una matriz de enteros
    0, 1 y 2. Si hay tableros de distintos niveles donde hay tanto X como O en posición [i][j], la casilla
    [i][j] de matriz_proyeccion es 3.
        """

        matriz:List[List[int]]=[]
        fila:List[int]=[]
        for i in range(self.lado):
            fila=[]
            for j in range(self.lado):
                fila.append(getattr(self.estado[0][i][j], "estado"))
            
            matriz.append(fila)

        #ahora vemos los niveles superiores
        matriz_backup = copy.deepcopy(matriz)

        for k in range(1, self.lado):
            for i in range(self.lado):
                for j in range(self.lado):
                    if getattr(self.estado[k][i][j], "estado") not in [0, matriz_backup[i][j]]:
                        matriz[i][j] == 3 #hay superposicion de estados
                    

        return matriz

    def actualizar_casilla(self, nivel:int, fila:int, columna:int):
        """Un método para actualizar el valor de una casilla,
        dependiendo de quién sea el jugador con el turno
        que la seleccione
        
        ### Argumentos
        * `nivel`: Un número de nivel en el tablero 3D
        * `fila`: Un número de fila válido en la matriz que representa el tablero
        * `columna`: Un número de columna válido en la matriz que representa el tablero

        ### Ejecución
        Accede a la casilla de posición [i][j] en el estado del tablero de nivel `nivel` y modifica su
        atributo estado para que refleje el jugador que la acaba de seleccionar.
        """

        casilla:'Casilla' = self.estado[nivel][fila][columna]
        if getattr(casilla, "estado") == 0: #está vacía, movimiento legal
            casilla.actualizar(self.turno)
        else: #no vacía
            raise ValueError("No se puede modificar una casilla no vacía")

    def movimientos_restantes(self)->int:
        """Un método que retorna la cantidad de movimientos restantes posibles
        a partir de la posición actual del tablero 3D.
        
        ### Retorno
        int: La cantidad de casillas vacías en el tablero."""

        lado:int = self.lado

        matriz = self.matriz_numerica()

        suma:int = 0
        for k in range(lado):
            for i in range(lado):
                for j in range(lado):
                    if matriz[k][i][j] == 0:
                        suma = suma + 1

        return suma

    def matriz_numerica(self)->List[List[List[int]]]:
        """Un método que devuelve la matriz numérica de estados asociados a cada casilla
    del tablero.
    
    ### Retorno
    List[List[List[int]]]: Una matriz NxNxN de lado N = lado del tablero que contiene
    en la entrada [i][j] el valor de `estado` de la Casilla de posición [nivel][i][j] de
    `estado` del tablero. En otras palabras, `matriz_numerica` retorna una hipermatriz de enteros
    0, 1 y 2.
        """

        matriz:List[List[List[int]]]=[]
        submatriz:List[List[int]]=[]
        fila:List[int]=[]
        for k in range(self.lado):
            submatriz = []
            for i in range(self.lado):
                fila=[]
                for j in range(self.lado):
                    fila.append(getattr(self.estado[k][i][j], "estado"))
                
                submatriz.append(fila)

            matriz.append(submatriz)

        return matriz