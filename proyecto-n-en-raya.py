#Este programa contiene el juego de N-en-raya-3D
import tkinter as tk
import logging
from typing import List, Tuple

logging.basicConfig(level=logging.DEBUG, filename="log.log", filemode = "w", format="%(levelname)s - %(message)s")
#Ahora cada vez que se ejecute main, se crea un archivo log.log que contiene el log

logging.info("Empieza la ejecución de proyecto-n-en-raya")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú Principal")

# Funciones para las opciones del menú
def iniciar_juego():
    logging.info("Se ejecuta iniciar_juego")
    print("El juego se está iniciando...")

def salir_del_juego():
    logging.info("Se ejecuta salir_del_juego")
    ventana.destroy()

# Crear los botones del menú
btn_iniciar = tk.Button(ventana, text="Iniciar Juego", command=iniciar_juego)
btn_iniciar.pack(pady=10)

btn_salir = tk.Button(ventana, text="Salir del Juego", command=salir_del_juego)
btn_salir.pack(pady=10)

# Mostrar la ventana
logging.info("Cargando ventana principal...")
ventana.mainloop()
