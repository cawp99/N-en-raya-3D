#Un archivo que contiene funciones necesarias para la ejecución del programa en consola
from typing import List

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