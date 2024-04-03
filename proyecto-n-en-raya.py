#Este programa contiene el juego de N-en-raya-3D
import tkinter as tk
import logging
from typing import List, Tuple
import clases
import verificaciones

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
    #print("El juego se está iniciando...")
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
        aceptar = tk.Button(err, text="Aceptar", command=err.destroy)
        aceptar.pack()
        
    
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

def eliminar_tableros():
    tableros.destroy()

def iniciar_tableros():
    global tableros 
    tableros = tk.Frame(main_frame)
    tableros.pack()

def reiniciar_tableros():
    eliminar_tableros()
    iniciar_tableros()

def menu_inicial():
    """Una función que muestra el menú inicial"""
    
    reiniciar_ventana()

    # Crear los botones del menú
    btn_iniciar = tk.Button(main_frame, text="Iniciar Juego", command=iniciar_juego)
    btn_iniciar.pack(pady=10)

    btn_salir = tk.Button(main_frame, text="Salir del Juego", command=salir_del_juego)
    btn_salir.pack(pady=10)

def empezar_juego(first:bool = True):
    """Genera el tablero y empieza el juego"""
    global Jugador1
    global Jugador2
    global tablero 
    global tableros
    global variable_nivel
    
    if first:
        Jugador1 = clases.Jugador(nombre_jug1, "X")
        Jugador2 = clases.Jugador(nombre_jug2, "O")

    tablero = clases.Tablero_3D(Jugador1, Jugador2, tamaño)
    #print("Juego creado")

    reiniciar_ventana()
    datos_tablero()

    #ahora creamos los tableros para los distintos niveles
    tableros = tk.Frame(main_frame)
    tableros.pack()

    variable_nivel = tk.IntVar()

    imprimir_tablero(0)

    btn_menu = tk.Button(main_frame, text="Menú Principal", command=menu_inicial)
    btn_menu.pack(side="bottom")


def nombre_del_turno()->str:
    """Devuelve el nombre del Jugador con el turno"""
    if getattr(tablero, 'turno') == 1:
        return getattr(Jugador1, 'nombre')
    else:
        return getattr(Jugador2, 'nombre')
    
def actualizar_nombre_turno():
    """Actualiza el nombre de la etiqueta label_turno"""
    label_turno.config(text=f"El turno actual es de {nombre_del_turno()}")
    label_turno.after(100, actualizar_nombre_turno)

def datos_tablero():
    """Imprime los datos del tablero y del turno actual"""
    global label_turno

    datos = tk.Frame(main_frame)
    datos.pack()

    label_jug1:tk.Label = tk.Label(datos, text=f"El jugador 1 es {getattr(Jugador1, 'nombre')}")
    label_jug1.grid(row=0, column=0, padx=10)

    label_jug1:tk.Label = tk.Label(datos, text=f"El jugador 2 es {getattr(Jugador2, 'nombre')}")
    label_jug1.grid(row=0, column=1, padx=10)

    label_puntaje_jug1:tk.Label = tk.Label(datos, text=f"Puntaje: {getattr(Jugador1, 'puntaje')}")
    label_puntaje_jug1.grid(row=1, column=0)

    label_puntaje_jug2:tk.Label = tk.Label(datos, text=f"Puntaje: {getattr(Jugador2, 'puntaje')}")
    label_puntaje_jug2.grid(row=1, column=1)


    frame_turno = tk.Frame(main_frame)
    frame_turno.pack()

    label_turno = tk.Label(frame_turno, text=f"El turno actual es de {nombre_del_turno()}")
    label_turno.pack()
    actualizar_nombre_turno()

def casilla_presionada(event): #solo para botones de casilla

    fila = event.widget.grid_info()['row']
    columna = event.widget.grid_info()['column']

    global variable_nivel
    
    nivel = variable_nivel.get()

    #print(f"Nivel de la casilla seleccionada: {nivel}")

    continue_exec = True

    estado = getattr(tablero, "estado")
    if getattr(estado[nivel][fila][columna], "estado") != 0:
        err=tk.Toplevel(ventana)
        err.title("3rr0r")
        msg=tk.Label(err, text="Ocurrió un error", fg="Red")
        msg.pack()
        msg2=tk.Label(err, text="No puedes seleccionar casillas ya seleccionadas")
        msg2.pack()
        aceptar = tk.Button(err, text="Aceptar", command=err.destroy)
        aceptar.pack()
        continue_exec = False

    if continue_exec:
        #print(f"Actualizamos la casilla {nivel},{fila},{columna}")
        tablero.actualizar_casilla(nivel, fila, columna)
        casilla_act = tablero.estado[nivel][fila][columna]
        estado_nuevo = getattr(casilla_act, 'estado')
        #print(f"estado de la casilla: {estado_nuevo}")
        event.widget.config(bg="seashell4")

        if getattr(tablero,"turno")==1:
            event.widget.config(text="X", fg="salmon")
        else:
            event.widget.config(text="O", fg="SkyBlue1")

        hipermatriz = tablero.matriz_numerica()
        matriz = tablero.matriz_proyeccion()
        mov_restantes = tablero.movimientos_restantes()
        turn = getattr(tablero,'turno')
        verificar_ganador(hipermatriz, matriz, mov_restantes, turn)

def verificar_ganador(hipermatriz:List[List[List[int]]], matriz:List[List[int]], movimientos:int, turn:int):
    """Verifica si alguien acaba de ganar en este turno"""

    candidato_ganador = verificaciones.hay_ganador(hipermatriz, matriz, turn)
    #print(str(hipermatriz))
    #print(f"hay candidato_ganador: {candidato_ganador}")
    if candidato_ganador == 0: #no hay ganador
        tablero.siguiente_turno()
        pass #continuamos
    elif candidato_ganador == 1: #gana el jugador de las X
        ventana_fin_de_ronda(1)
        tablero.jugadores[0].ganar_punto()
    elif candidato_ganador == 2: #gana el jugador de las O
        ventana_fin_de_ronda(2)
        tablero.jugadores[1].ganar_punto()

    #verificamos si ya no hay más movimientos legales
    if movimientos == 0:
        ventana_fin_de_ronda(0)

def imprimir_tablero(n: int):
    """Imprime el tablero de nivel `n` con menús para cada casilla:"""

    global variable_nivel

    frame_botones = tk.Frame(tableros, pady=20)
    frame_botones.pack(side="bottom")

    ventana.update()

    info_nivel = tk.Frame(tableros)
    info_nivel.pack()

    label_nivel = tk.Label(info_nivel, text=f"Nivel {n}")
    label_nivel.pack(pady=10)

    btns_nivel = tk.Frame(info_nivel)
    btns_nivel.pack()
    btn_subir_nivel = tk.Button(info_nivel, text="Subir nivel", command=subir_nivel)
    btn_subir_nivel.pack(side="right", padx=10)
    btn_bajar_nivel = tk.Button(info_nivel, text="Bajar nivel", command=bajar_nivel)
    btn_bajar_nivel.pack(side="left", padx=10)

    for i in range(tamaño):
        for j in range(tamaño):
            boton = tk.Button(frame_botones, text = " ", padx=5, pady=5)
            boton.grid(row=i, column=j)
            boton.bind("<Button-1>", casilla_presionada)
            #inicializamos con el valor correspondiente
            hipermatriz = tablero.matriz_numerica()
            if hipermatriz[n][i][j] == 1:
                boton.config(text="X", fg="salmon", bg="seashell4")
            elif hipermatriz[n][i][j] == 2:
                boton.config(text="O", fg="SkyBlue1", bg="seashell4")



def subir_nivel():
    global variable_nivel

    do_nothing = False

    nivel = variable_nivel.get()
    if nivel == tamaño - 1:
        do_nothing = True

    if not do_nothing:
        variable_nivel.set(nivel + 1)
        nivel = nivel + 1 
        reiniciar_tableros()
        imprimir_tablero(nivel)

def bajar_nivel():
    global variable_nivel

    do_nothing = False

    nivel = variable_nivel.get()
    if nivel == 0:
        do_nothing = True

    if not do_nothing:
        variable_nivel.set(nivel - 1)
        nivel = nivel - 1 
        reiniciar_tableros()
        imprimir_tablero(nivel)

def ventana_fin_de_ronda(n:int):
    """
    Se abre una ventana que indica el resultado del juego.

    ### Argumento
    * n: 0 si es empate, 1 si ganó el Jugador 1, 2 si ganó el Jugador 2.

    ### Variable global
    * vg: La ventana de fin de ronda
    """
    global vg

    txt : str = ""
    if n == 0:
        txt = "Empate"
    elif n == 1:
        txt = f"¡Ganó {getattr(Jugador1, 'nombre')}!"
    elif n== 2:
        txt = f"¡Ganó {getattr(Jugador2, 'nombre')}!"

    vg = tk.Toplevel(ventana)
    vg.title("Ronda terminada")
    vg.geometry("100x100")
    msg_label = tk.Label(vg, text=txt)
    msg_label.pack()

    btn_continuar = tk.Button(vg, text="Continuar", command=continuar)
    btn_menu = tk.Button(vg, text="Menú Principal", command=menu_inicial_vg)
    btn_continuar.pack()
    btn_menu.pack()

    reiniciar_ventana()

def menu_inicial_vg():
    menu_inicial()
    vg.destroy()

def continuar():
    """Función para cuando se quiere continuar entre rondas"""

    global Jugador1
    global Jugador2

    [Jugador1, Jugador2] = [Jugador2, Jugador1] #se cambian los nombres
    vg.destroy()
    empezar_juego(False)

menu_inicial()

# Mostrar la ventana
logging.info("Cargando ventana principal...")
ventana.mainloop()
