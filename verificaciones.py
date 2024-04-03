# Un archivo que contenga las funciones de verificación para la matriz

from typing import List
import logging

def hay_ganador(hipermatriz:List[List[List[int]]], matriz:List[List[int]], turn:int)->int:
    """
    Una función que recibe un tablero e indica si hay un ganador.

    ### Argumentos
    * `hipermatriz`: Una matriz 3D NxNxN de enteros 0, 1, 2.
    * `matriz`: Una matriz numérica, como el resultado del método `matriz_numerica`
    de la clase Tablero_2D

    ### Retorno
    int: 0 si no hay ganador, 1 si gana el jugador que tiene las "X", 2 si gana el 
    jugador que tiene las "O"
    """
    logging.info("se ejecuta hay_ganador")
    logging.debug("hipermatriz:")
    logging.debug(str(hipermatriz))
    logging.debug("matriz")
    logging.debug(str(matriz))

    victorias=verificacion_completa(hipermatriz, matriz)

    logging.debug("victorias: " + str(victorias))

    if len(victorias) == 0:
        return 0
    
    #si hay algunas filas o columnas o diagonales de entradas iguales
    for linea in victorias:
        logging.debug(f"linea es {str(linea)}")

        #extraemos la linea, columna, diagonal, diagonal inversa, intertablero
        queue : List[int] = []

        if linea[0]==1: #se trata de una fila
            for i in range(len(matriz)):
                queue.append(matriz[linea[1]][i])

            if queue[0] == 0:
                continue #ignora si son filas de entradas iguales vacías
            elif queue[0] != 3:
                return turn
            elif queue[0] == 3:
                if (1 not in queue) and (2 not in queue):
                    continue #vacía
            
        elif linea[0]==2: #se trata de una columna
            for i in range(len(matriz)):
                queue.append(matriz[i][linea[1]])

            if matriz[0][linea[1]] == 0:
                continue #ignora si son columnas de entradas iguales vacías
            elif queue[0] != 3:
                return turn
            elif queue[0] == 3:
                if (1 not in queue) and (2 not in queue):
                    continue #vacía
            
        elif linea[0]==3: #diagonal principal
            for i in range(len(matriz)):
                queue.append(matriz[i][i])

            if matriz[0][0] == 0:
                continue #ignora si son digonales de entradas iguales vacías
            elif queue[0] != 3:
                return turn
            elif queue[0] == 3:
                if (1 not in queue) and (2 not in queue):
                    continue #vacía
            
        elif linea[0]==4: #diagonal secundaria
            for i in range(len(matriz)):
                queue.append(matriz[len(matriz)-1-i][i])

            if matriz[len(matriz)-1][0] == 0:
                continue #ignora si son digonales de entradas iguales vacías
            elif queue[0] != 3:
                return turn
            elif queue[0] == 3:
                if (1 not in queue) and (2 not in queue):
                    continue #vacía
            
        elif linea[0]==5: #linea intertablero
            logging.debug("linea intertablero")
            fila = linea[1]
            columna = linea[2]
            logging.debug(f"fila {fila}, columna {columna}")
            if hipermatriz[0][fila][columna] == 0:
                continue #ignora interlineas nulas
            else:
                logging.debug(f"victoria! para {turn}")
                return turn
            


    #no se activa ningun return
    return 0 #no hay ganador 

def verificacion_horizontal(matriz:List[List[int]], fila:int)->bool:
    """
    Una función que verifica si una fila en una matriz tiene todas sus entradas iguales.

    ### Argumentos
    * `matriz`: Una matriz cuadrada de enteros
    * `fila`: Un índice entero que representa un número de fila

    ### Retorno
    bool: True si la fila con índice `fila` tiene todas sus entradas iguales (incluyendo 3). 
    False en caso contrario.
    """

    if fila not in range(len(matriz)):
        raise ValueError("El número de fila no es válido")
    
    # creamos elemento para comparar

    comparar = 3 #valor base
    for i in matriz[fila]:
        if i != 3:
            comparar = i
            break

    for i in range(1, len(matriz)):
        if matriz[fila][i] == 3:
            pass
        elif matriz[fila][i] != comparar:
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
    
    
    comparar = 3 #valor base
    for i in range(len(matriz)):
        if matriz[i][columna] != 3:
            comparar = matriz[i][columna]
            break

    for i in range(1, len(matriz)):
        if matriz[i][columna] == 3:
            pass
        elif matriz[i][columna] != comparar:
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

    comparar = 3 #valor base
    for i in range(len(matriz)):
        if matriz[i][i] != 3:
            comparar = matriz[i][i]
            break

    for i in range(1,len(matriz)):
        if matriz[i][1] == 3:
            pass
        elif matriz[i][i] != comparar:
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

    comparar = 3 #valor base
    for i in range(len(matriz)):
        if matriz[len(matriz)-1-i][i] != 3:
            comparar = matriz[len(matriz)-1-i][i]
            break

    for i in range(1,len(matriz)):
        if matriz[len(matriz)-1-i][i] == 3:
            pass
        elif matriz[len(matriz)-1-i][i] != comparar:
            return False
        
    return True

def verificacion_intertablero(hipermatriz:List[List[List[int]]], fila:int, columna:int)->bool:
    """
    Una función que verifica si en la posición [fila][columna] hay una línea
    intertablero que tiene entradas iguales.

    ### Argumentos
    * `hipermatriz`: Una hipermatriz NxNxN
    * `fila`: Numero de fila
    * `columna`: Numero de columna

    ### Retorno
    bool: True si hay una línea intertablero en la posición [fila][columna]. False
    en caso contrario.
    """

    comparar = hipermatriz[0][fila][columna] #caso base

    for k in range(1, len(hipermatriz)):
        if hipermatriz[k][fila][columna] != comparar:
            return False
        
    return True #else

def verificacion_completa(hipermatriz:List[List[List[int]]], matriz:List[List[int]])->List[List[int]]:
    """
    Una función que verifica si alguna de las columnas, filas o diagonales
    de una matriz tienen entradas iguales y produce una lista con estas
    líneas iguales. Tambien verifica si en la hipermatriz hay lineas
    iguales y añade a la lista estas posiciones.

    ### Argumento
    * `hipermatriz`: List[List[List[int]]] : Una matriz NxNxN de enteros
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
    #verificaciones en la matriz 2D
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

    #verificaciones en la matriz 3D
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if verificacion_intertablero(hipermatriz, i, j):
                logging.debug(f"linea intertablero encontrada: {i},{j}")
                retorno.append([5, i, j])


    return retorno



