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


def casilla_en_consola(casilla:'Casilla')->str:
    """Una función para imprimir el estado de la casilla pero
    de manera visual.
    
    ### Argumento
    * `casilla`: Una casilla de la clase Casilla.
    
    ### Retorno
    * str: "-" si el estado es 0, "X" si el estado es 1, "O" si el estado es 2."""

    estado:int = getattr(casilla, "estado")
    if estado == 0:
        return "-"
    elif estado == 1:
        return "X"
    else:
        return "O"
    
def tablero_en_consola(tablero:'Tablero_2D')->None:
    """Imprime el estado del tablero almacenado, apropiadamente de 
    acuerdo a casilla_en_consola.
    
    ### Argumento
    * `tablero`: Un objeto de la clase Tablero_2D

    ### Ejecución
    Imprime un arreglo cuadrado del mismo lado que el lado del tablero. Cada
    casilla tiene un caracter correspondiente al estado de la casilla de esa posición.
    En los bordes se muestran las coordenadas X, Y para seleccionar una casilla.
    """

    lado:int = getattr(tablero, "lado")
    estado:List[List['Casilla']] = getattr(tablero, "estado")

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
    tablero = Tablero_2D(jugador1,jugador2,N) 
    logging.debug("El turno actual vale: " + str(getattr(tablero, "turno")))       
    
    finalizado:bool = False
    while not finalizado:
        print("Estado del juego:")
        imprimir_tablero(tablero)
        break
        
