#Este programa contiene el juego de N-en-raya-3D
import tkinter as tk
import logging
from typing import List, Tuple
import clases

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
    pedir_datos()

def salir_del_juego():
    """Función para finalizar el juego"""
    logging.info("Se ejecuta salir_del_juego")
    ventana.destroy()

def pedir_datos():
    """Una función que muestra el menú para pedir los datos del juego
    """
    global nombre1
    global nombre2
    global entry_tamaño

    datos = tk.Frame(main_frame)
    datos.pack()

    nombres = tk.Frame(datos)
    nombres.pack()

    pedir_nombre1:tk.Label = tk.Label(nombres, text="Nombre del Jugador 1: ")
    pedir_nombre2:tk.Label = tk.Label(nombres, text="Nombre del Jugador 2: ")
    pedir_nombre1.grid(row=0, column=0)
    pedir_nombre2.grid(row=1, column=0)

    nombre1 = tk.Entry(nombres)
    nombre2 = tk.Entry(nombres)
    nombre1.grid(row=0, column=1)
    nombre2.grid(row=1, column=1)

    pedir_tamaño:tk.Label = tk.Label(nombres, text="Lado del tablero (N > 2): ")
    pedir_tamaño.grid(row = 2, column=0, pady=10)
    entry_tamaño = tk.Entry(nombres)
    entry_tamaño.grid(row=2, column=1)


    nombres_bottom = tk.Frame(datos, pady=20)
    nombres_bottom.pack()

    boton_iniciar:tk.Button = tk.Button(nombres_bottom, text = "Iniciar", command=guardar_datos)
    boton_iniciar.pack()
    boton_regresar:tk.Button = tk.Button(nombres_bottom, text = "Regresar", command=menu_inicial)
    boton_regresar.pack()

def guardar_nombres():
    """Una función para guardar los nombres desde el botón de Iniciar
    
    ### Crea variables globales
    * `nombre_jug1`: El nombre del jugador 1 (str)
    * `nombre_jug2`: El nombre del jugador 2 (str)
    """

    global nombre_jug1
    global nombre_jug2
    nombre_jug1 = nombre1.get()
    nombre_jug2 = nombre2.get()


def guardar_tamaño()->int:
    """Una función para guardar el tamaño del tablero
    
    ### Crea variable global
    * `tamaño`: El lado del tablero (int)
    """

    global entry_tamaño
    global tamaño

    tamaño_temp = entry_tamaño.get()
    try:
        tamaño_temp = int(tamaño_temp)
    except:
        raise TypeError("El lado no es un entero")
    
    if tamaño_temp <= 2:
        raise ValueError("El lado debe ser mayor que 2.")
    
    tamaño = tamaño_temp

def guardar_datos()->bool: 
    """Una función para guardar los datos y empezar el juego
    """

    datos_guardados = False

    guardar_nombres()
    try:
        guardar_tamaño()
    except Exception as e:
        err=tk.Toplevel(ventana)
        err.title("3rr0r")
        msg=tk.Label(err, text="Ocurrió un error", fg="Red")
        msg.pack()
        msg2=tk.Label(err, text=e)
        msg2.pack()
        
    
    datos_guardados = True 

    if not datos_guardados:
        pass
    else:
        empezar_juego()

def eliminar_ventana():
    main_frame.destroy()

def iniciar_ventana():
    global main_frame 
    main_frame = tk.Frame(ventana)
    main_frame.pack()

def reiniciar_ventana():
    eliminar_ventana()
    iniciar_ventana()

def menu_inicial():
    """Una función que muestra el menú inicial"""
    
    reiniciar_ventana()

    # Crear los botones del menú
    btn_iniciar = tk.Button(main_frame, text="Iniciar Juego", command=iniciar_juego)
    btn_iniciar.pack(pady=10)

    btn_salir = tk.Button(main_frame, text="Salir del Juego", command=salir_del_juego)
    btn_salir.pack(pady=10)

def empezar_juego():
    """Genera el tablero y empieza el juego"""
    global Jugador1
    global Jugador2
    global tablero 
    
    Jugador1 = clases.Jugador(nombre_jug1, "X")
    Jugador2 = clases.Jugador(nombre_jug2, "O")
    tablero = clases.Tablero_2D(Jugador1, Jugador2, tamaño)
    print("Juego creado")

    reiniciar_ventana()
    datos_tablero()


def nombre_del_turno()->str:
    """Devuelve el nombre del Jugador con el turno"""
    if getattr(tablero, 'turno') == 1:
        return getattr(Jugador1, 'nombre')
    else:
        return getattr(Jugador2, 'nombre')
    
def actualizar_nombre_turno():
    """Actualiza el nombre de la etiqueta label_turno"""
    label_turno.config(text=f"El turno actual es de {nombre_del_turno()}")

def datos_tablero():
    """Imprime los datos del tablero y del turno actual"""
    global label_turno

    datos = tk.Frame(main_frame)
    datos.pack()

    label_jug1:tk.Label = tk.Label(datos, text=f"El jugador 1 es {getattr(Jugador1, 'nombre')}")
    label_jug1.pack(side="left", padx=10)

    label_jug1:tk.Label = tk.Label(datos, text=f"El jugador 2 es {getattr(Jugador2, 'nombre')}")
    label_jug1.pack(side="right", padx=10) 

    frame_turno = tk.Frame(main_frame)
    frame_turno.pack()

    label_turno = tk.Label(frame_turno, text=f"El turno actual es de {nombre_del_turno()}")
    label_turno.pack()
    label_turno.after(100, actualizar_nombre_turno)


menu_inicial()

# Mostrar la ventana
logging.info("Cargando ventana principal...")
ventana.mainloop()
