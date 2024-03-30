#Este programa contiene el juego de N-en-raya-3D
import tkinter as tk
import logging
from typing import List, Tuple

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode = "w", format="%(levelname)s - %(message)s")
#Ahora cada vez que se ejecute main, se crea un archivo log.log que contiene el log

logging.info("Empieza la ejecución de proyecto-n-en-raya")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("N en raya 3D")
ventana.geometry("600x600")

#contenedor principal
main_frame : tk.Frame = tk.Frame(ventana)
main_frame.pack()

# Funciones para las opciones del menú
def iniciar_juego():
    """Función para iniciar el juego"""
    reiniciar_ventana()
    logging.info("Se ejecuta iniciar_juego")
    print("El juego se está iniciando...")
    pedir_nombres()

def salir_del_juego():
    """Función para finalizar el juego"""
    logging.info("Se ejecuta salir_del_juego")
    ventana.destroy()

def pedir_nombres():
    """Una función para pedir los nombres de los Jugadores"""
    nombres = tk.Frame(main_frame)
    nombres.pack()

    pedir_nombre1:tk.Label = tk.Label(nombres, text="Nombre del Jugador 1: ")
    pedir_nombre2:tk.Label = tk.Label(nombres, text="Nombre del Jugador 2: ")
    pedir_nombre1.grid(row=0, column=0)
    pedir_nombre2.grid(row=1, column=0)
    nombre_jugador1:tk.Entry = tk.Entry(nombres)
    nombre_jugador2:tk.Entry = tk.Entry(nombres)
    boton_nombres:tk.Button = tk.Button(nombres, text = "Listo")
    nombre_jugador1.grid(row=0, column=1)
    nombre_jugador2.grid(row=1, column=1)
    boton_nombres.grid(row=2, column=0, padx=20)

    

def eliminar_ventana():
    main_frame.destroy()

def iniciar_ventana():
    global main_frame 
    main_frame = tk.Frame(ventana)
    main_frame.pack()

def reiniciar_ventana():
    eliminar_ventana()
    iniciar_ventana()




# Crear los botones del menú
btn_iniciar = tk.Button(main_frame, text="Iniciar Juego", command=iniciar_juego)
btn_iniciar.pack(pady=10)

btn_salir = tk.Button(main_frame, text="Salir del Juego", command=salir_del_juego)
btn_salir.pack(pady=10)

# Mostrar la ventana
logging.info("Cargando ventana principal...")
ventana.mainloop()
