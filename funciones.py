#Un archivo que contiene funciones necesarias para la ejecución del programa en consola
from typing import List
from clases import Tablero_2D, Casilla, Jugador
import logging

def pedir_nombres()->List[str]:
    """Una función para pedir los nombres de los jugadores a partir de la entrada.
    
    ### Retorno
    * `List[str]`: Una lista con los nombres de los dos jugadores en orden (strings).

    ### Excepciones
    * Si los nombres son iguales, se lanza la excepción ValueError
    """

    print("¿Quiénes están jugando?")
    nombre1:str = input("Escriba el nombre del Jugador 1: ")
    nombre2:str = input("Escriba el nombre del Jugador 2: ")

    if nombre2 == nombre1:
        raise ValueError("¡Los nombres de Jugadores no pueden ser iguales!")
    
    return [nombre1, nombre2]

def pedir_tamaño()->int:
    """Una función para pedir el tamaño N del lado del tablero.
    
    ### Retorno
    *`int`: Un entero que representa el lado del tablero N > 2

    ### Excepciones
    * Si N <= 2 se arroja ValueError.
    """

    print("¿Cuál será el lado N del tablero? (N > 2)")
    tamaño = input("Escriba el lado N: ")

    try:
        tamaño = int(tamaño)
    except:
        raise TypeError("El tamaño no es entero")
    
    if tamaño <= 2:
        raise ValueError("El tamaño debe ser N > 2")
    
    return tamaño

def imprimir_tablero(tablero:'Tablero_2D') -> None:
    """Una función para imprimir el tablero actual, incluyendo toda la información
    necesaria y una grilla correspondiente al juego.

    ### Argumento
    * `tablero`: Un objeto de la clase Tablero_2D

    ### Ejecución
    Al ejecutarse esta función, se imprimen los nombres de los jugadores, quien tiene
    el turno y una grilla correspondiente al estado actual del tablero.
    """

    logging.info("Se ejecuta la función imprimir_tablero")
    jugadores = getattr(tablero, "jugadores")
    print("Jugador 1: " + getattr(jugadores[0], "nombre"))
    print("Puntaje: " + str(getattr(jugadores[0], "puntaje")))
    print("Jugador 2: " + getattr(jugadores[1], "nombre"))
    print("Puntaje: " + str(getattr(jugadores[1], "puntaje")))

    print("El turno actual es de ", end = "")
    if getattr(tablero, "turno") == 1:
        print(getattr(jugadores[0], "nombre"))
    else:
        print(getattr(jugadores[1], "nombre"))

    tablero_en_consola(tablero)


def casilla_en_consola(n:int)->str:
    """Una función para imprimir el estado de la casilla pero
    de manera visual.
    
    ### Argumento
    * `n`: Entero que representa el estado de una casilla.
    
    ### Retorno
    * str: "-" si `n` es 0, "X" si `n` es 1, "O" si `n` es 2."""


    if n == 0:
        return "-"
    elif n == 1:
        return "X"
    else:
        return "O"
    
def tablero_en_consola(tablero:'Tablero_2D')->None:
    """Imprime el estado del tablero almacenado, apropiadamente de 
    acuerdo a casilla_en_consola.
    
    ### Argumento
    * `tablero`: Un objeto de la clase Tablero_2D

    ### Ejecución
    Imprime un arreglo cuadrado lado 2 más que el lado del tablero. Cada
    casilla tiene un caracter correspondiente al estado de la casilla de esa posición.
    En los bordes se muestran las coordenadas X, Y para seleccionar una casilla.
    """

    lado:int = getattr(tablero, "lado")
    estado:List[List[int]] = tablero.matriz_numerica()

    for i in range(lado+2):
        for j in range(lado+2):
            if i == 0 or i == lado+1:
                if j == 0:
                    print(" ", end = " ")
                elif j == lado + 1:
                    print("")
                else:
                    print(str(j), end = " ")

            else:
                if j == 0:
                    print(str(i), end = " ")
                elif j == lado +1:
                    print(str(i))
                else:
                    print(casilla_en_consola(estado[i-1][j-1]), end=" ")

    
def jugar(jugador1:'Jugador', jugador2:'Jugador', N:int)->None:
    """La función para jugar propiamente UNA RONDA del juego.
    
    ### Argumentos
    * `jugador1`: Un jugador de la clase Jugador.
    * `jugador2`: Un jugador de la clase Jugador.
    * `N`: Un entero N>2 que representa el lado del tablero
    
    ### Ejecución
    Empieza el juego, se ejecuta un bucle turno por turno en donde se imprime la 
    información relevante al estado del juego actual, y sale un menú donde se
    puede escoger la casilla seleccionada por el turno correspondiente.
    
    El bucle continúa hasta que se haya logrado terminar la partida. En ese caso,
    si hay un ganador, se incrementa su puntaje en 1 punto. 
    """

    logging.info("Empieza el juego")
    tablero : 'Tablero_2D'= Tablero_2D(jugador1,jugador2,N)
    matriz : List[List[int]] = []
    logging.debug("El turno actual vale: " + str(getattr(tablero, "turno")))       
    
    juego_finalizado:bool = False
    candidato_ganador:int = -1
    while not juego_finalizado:
        print("Estado del juego:")
        imprimir_tablero(tablero)
        
        indices:List[int] = pedir_movimiento()
        tablero.actualizar_casilla(indices[0], indices[1])

        matriz = tablero.matriz_numerica()

        candidato_ganador = hay_ganador(matriz)
        if candidato_ganador == 0: #no hay ganador
            tablero.siguiente_turno()
            continue
        elif candidato_ganador == 1: #gana el jugador de las X
            juego_finalizado = True
            print("Ronda finalizada, el ganador es " + getattr(tablero.jugadores[0], "nombre"))
            tablero_en_consola(tablero)
        elif candidato_ganador == 2: #gana el jugador de las O
            juego_finalizado = True
            print("Ronda finalizada, el ganador es " + getattr(tablero.jugadores[1], "nombre"))
            tablero_en_consola(tablero)
        
def verificacion_horizontal(matriz:List[List[int]], fila:int)->bool:
    """
    Una función que verifica si una fila en una matriz tiene todas sus entradas iguales.

    ### Argumentos
    * `matriz`: Una matriz cuadrada de enteros
    * `fila`: Un índice entero que representa un número de fila

    ### Retorno
    bool: True si la fila con índice `fila` tiene todas sus entradas iguales. 
    False en caso contrario.
    """

    if fila not in range(len(matriz)):
        raise ValueError("El número de fila no es válido")
    
    
    for i in range(1, len(matriz)):
        if matriz[fila][i] != matriz[fila][i-1]:
            return False
        
    return True #solo si son iguales

def verificacion_vertical(matriz:List[List[int]], columna:int)->bool:
    """
    Una función que verifica si una columna en una matriz tiene todas 
    sus entradas iguales.

    ### Argumentos
    * `matriz`: Una matriz cuadrada de enteros
    * `columna`: Un índice entero que representa un número de fila

    ### Retorno
    bool: True si la columna con índice `columna` tiene todas sus entradas iguales. 
    False en caso contrario.
    """

    if columna not in range(len(matriz)):
        raise ValueError("El número de fila no es válido")
    
    
    for i in range(1, len(matriz)):
        if matriz[i][columna] != matriz[i-1][columna]:
            return False
        
    return True #solo si son iguales


def verificacion_diagonal(matriz:List[List[int]])->bool:
    """
    Una función que verifica si la diagonal principal en una matriz tiene 
    todas sus entradas iguales.

    ### Argumentos
    * `matriz`: Una matriz cuadrada de enteros

    ### Retorno
    bool: True si la diagonal principal tiene todas las entradas iguales. False
    en caso contrario
    """

    for i in range(1,len(matriz)):
        if matriz[i][i] != matriz[i-1][i-1]:
            return False
        
    return True

def verificacion_diagonal_inversa(matriz:List[List[int]])->bool:
    """
    Una función que verifica si la diagonal secundaria (inversa) en una matriz tiene 
    todas sus entradas iguales.

    ### Argumentos
    * `matriz`: Una matriz cuadrada de enteros

    ### Retorno
    bool: True si la diagonal secundaria tiene todas las entradas iguales. False
    en caso contrario
    """

    for i in range(1,len(matriz)):
        if matriz[len(matriz)-1-i][i] != matriz[len(matriz)-i][i-1]:
            return False
        
    return True

def verificacion_completa(matriz:List[List[int]])->List[List[int]]:
    """
    Una función que verifica si alguna de las columnas, filas o diagonales
    de una matriz tienen entradas iguales y produce una lista con estas
    líneas iguales.

    ### Argumento
    * `matriz`: List[List[int]]: Una matriz cuadrada de enteros

    ### Retorno
    List[List[int]]: Una lista que contiene listas de enteros.
    Si la lista está vacía, ninguna diagonal, columna o fila tiene entradas iguales.

    Si la lista está no vacía, el primer elemento de una lista dentro del retorno
    vale 1 si se corresponde con una fila, 2 si se corresponde con una columna, 
    3 si es la diagonal principal y 4 si es la diagonal secundaria.
    En las listas dentro del retorno con primeras entradas 1 o 2 (filas o columnas),
    la segunda entrada es el número de fila (o columna, respectivamente) correspondiente
    que tiene entradas iguales. Si la primera entrada de la lista dentro del retorno
    es 3 o 4 (diagonales), las segundas entradas valen -1.
    """

    retorno : List[List[int]] = []
    for i in range(len(matriz)):
        if verificacion_horizontal(matriz, i):
            retorno.append([1, i])
    
    for i in range(len(matriz)):
        if verificacion_vertical(matriz, i):
            retorno.append([2, i])

    if verificacion_diagonal(matriz):
        retorno.append([3,-1])
    
    if verificacion_diagonal_inversa(matriz):
        retorno.append([4, -1])

    return retorno

def hay_ganador(matriz:List[List[int]])->int:
    """
    Una función que recibe un tablero e indica si hay un ganador.

    ### Argumento
    * `matriz`: Una matriz numérica, como el resultado del método `matriz_numerica`
    de la clase Tablero_2D

    ### Retorno
    int: 0 si no hay ganador, 1 si gana el jugador que tiene las "X", 2 si gana el 
    jugador que tiene las "O"
    """

    victorias=verificacion_completa(matriz)
    if len(victorias) == 0:
        return 0
    
    #si hay algunas filas o columnas o diagonales de entradas iguales
    for linea in victorias:
        if linea[0]==1: #se trata de una fila
            if matriz[linea[1]][0] == 0:
                continue #ignora si son filas de entradas iguales vacías
            elif matriz[linea[1]][0] == 1:
                return 1
            else:
                return 2
            
        elif linea[0]==2: #se trata de una columna
            if matriz[0][linea[1]] == 0:
                continue #ignora si son columnas de entradas iguales vacías
            elif matriz[0][linea[1]] == 1:
                return 1
            else:
                return 2
            
        elif linea[0]==3: #diagonal principal
            if matriz[0][0] == 0:
                continue #ignora si son digonales de entradas iguales vacías
            elif matriz[0][0] == 1:
                return 1
            else:
                return 2
            
        elif linea[0]==4: #diagonal secundaria
            if matriz[len(matriz)-1][0] == 0:
                continue #ignora si son digonales de entradas iguales vacías
            elif matriz[len(matriz)-1][0] == 1:
                return 1
            else:
                return 2

    #no se activa ningun return
    return 0 #no hay ganador 

def pedir_movimiento()->List[int]:
    """Una función para pedir las coordenadas de una casilla, que
    será usada para actualizar el estado del tablero y finalizar el turno.

    ### Parámetro
    * `lado`: Un entero que representa el lado N de la matriz NxN del tablero.

    ### Retorno
    List[int]: Una lista de dos enteros [i,j] que representan los índices de la
    casilla cuyas coordenadas fueron introducidas por el usuario.
    """

    print("""Escriba las coordenadas (X,Y) tal como se ven en la grilla
para ser marcada en su turno.""")
    x:str = int(input("Coordenada X horizontal: "))
    y:str = int(input("Coordenada Y vertical: "))

    retorno:List[int] = [y-1, x-1]
    return retorno
