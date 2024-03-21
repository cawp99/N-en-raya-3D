#Este será el archivo principal de una implementación del juego en 2D pero
#en consola únicamente. El objetivo es que con este juego funcional,
#se pueda simplemente pasar la parte grafica con tkinter como algo adicional
#y modificable

import clases
import funciones
import logging

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode = "w", format="%(levelname)s - %(message)s")
logging.info("Se inicia el programa")

print("¡Bienvenido al juego N en raya 2D (versión de consola)!")

#menú principal
entry:str = ""
while True:
    logging.debug("Nueva iteración del menú principal")
    print("MENÚ PRINCIPAL")
    print("""Opciones disponibles:
        1: Jugar
        2: Salir""")
    print("Escriba una opción: ", end = "")
    entry = input()

    logging.debug(f"entry vale {entry}")
    if entry == "1":
        logging.info("Se inicia el juego...")
        #jugar
        print("Se inicia el juego...")
        #seleccion de nombres
        logging.info("Se piden nombres de jugadores...")
        while True:
            try:
                nombres = funciones.pedir_nombres()
            except Exception as e:
                logging.exception("Ocurrió un error")
                print(e)
                continue #al menú principal

            #se crean los jugadores
            try:
                jugador1 = clases.Jugador(nombres[0], "X")
                jugador2 = clases.Jugador(nombres[1], "O")
            except Exception as e:
                logging.exception("Ocurrió un error")
                print(e)
                continue 

            break #Jugadores ya creados

        logging.info("Jugadores exitosamente creados")


        logging.info("Se pide el tamaño del tablero")
        #selección de tamaño
        N : int = 0
        while True:
            try:
                N = funciones.pedir_tamaño()
            except Exception as e:
                logging.exception("Ocurrió un error")
                print(e)
                continue

            break #tamaño exitosamente guardado

        logging.info("Dimensiones del tablero exitosamente guardadas")

        print("")
        print("Estos son los datos del juego:")
        print("JUGADOR 1")
        jugador1.estado()
        print("")
        print("JUGADOR 2")
        jugador2.estado()
        print("")
        print(f"Se jugará en un tablero {N}x{N}")

        #menú secundario
        secundario:bool = True
        while secundario:
            print("""¡Ya todo está listo para jugar! Opciones disponibles:
        1. Regresar
        2. Iniciar juego
                """)
            entry2 : str = input("Seleccione una opción: ")
            logging.debug(f"entry2 vale {entry2}")
            
            if entry2 == "1":
                secundario = False #regresa al menú principal

            elif entry2 == "2":
                print("Empieza el juego...")
                secundario = False
                loop_rondas:bool = True
                entry_rondas:str = ""
                while loop_rondas:
                    funciones.jugar(jugador1, jugador2, N)
                    print("¿Desea seguir jugando? 1: Sí. 2: Salir.")
                    entry_rondas=input("Escoga una opción: ")
                    if entry_rondas=="1":
                        [jugador1, jugador2] = [jugador2, jugador1] #se cambian puestos
                        print("NUEVA RONDA")
                        continue #siguiente ronda
                    elif entry_rondas=="2":
                        loop_rondas = False
                        secundario = False



            else:
                print("Opción no válida")
                continue


    elif entry == "2":
        logging.info("El usuario sale del juego...")
        #salir
        break

    else:
        logging.error("Opción no válida")
        print("Opción no válida")
        continue




#fuera del juego
print("¡Gracias por jugar!")
logging.info("Programa finalizado")