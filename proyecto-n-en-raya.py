#Este programa contiene el juego de N-en-raya-3D
import tkinter as tk
from typing import List, Tuple

def iniciar_juego():
    print("El juego se está iniciando...")

def salir_del_juego():
    ventana.destroy()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Menú Principal")

# Funciones para las opciones del menú
def iniciar_juego():
    print("El juego se está iniciando...")

def salir_del_juego():
    ventana.destroy()

# Crear los botones del menú
btn_iniciar = tk.Button(ventana, text="Iniciar Juego", command=iniciar_juego)
btn_iniciar.pack(pady=10)

btn_salir = tk.Button(ventana, text="Salir del Juego", command=salir_del_juego)
btn_salir.pack(pady=10)

etiqueta_jesus = tk.Label(ventana, text="Jesús estuvo aquí")
etiqueta_jesus.config(fg="yellow", bg="red", font=("Arial", 50, "bold"))
etiqueta_jesus.pack()

# Mostrar la ventana
ventana.mainloop()