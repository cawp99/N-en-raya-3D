#Un archivo que contiene las clases necesarias para el proyecto

class Jugador():
    """Una clase que almacene el Jugador, nombre, puntaje y que tipo de ficha juega.

    ### Atributos
    * `nombre`: Una string no vacía, el nombre del jugador
    * `ficha_actual`: Una string no vacía con dos valores: "X", "O". Representa
    el tipo de ficha que juega el jugador en cada partida.
    * `puntaje`: Un entero no negativo que representa la cantidad de partidas
    ganadas de este jugador.

    ### Métodos
    * Para cada atributo, métodos respectivos `get_atributo` y `set_atributo` que
    acceden al valor de un atributo y lo modifican, respectivamente.
    * `estado`: Imprime el estado actual del Jugador incluyendo todos sus atributos.
    * `ganar_punto`: Aumenta el valor de `puntaje` por 1.
    * `cambiar_ficha`: Cambia el valor de `ficha_actual` por el otro valor ("X" <-> "O")
    """

    def __init__(self, nombre:str, ficha_actual:str)->'Jugador':
        """Crea instancias de Jugador.
        
        ### Argumentos
        * `nombre`: Una string
        * `ficha_actual`: Una string "X" ó "O"

        ### Retorno
        Una instancia de Jugador con los atributos asignados por los parámetros nombre y 
        ficha_actual. El atributo puntaje = 0.

        ### Excepciones
        * Si `nombre` es vacío, lanza ValueError.
        * Si `ficha_actual` es distinta a "X" ó "O" lanza ValueError.

        ### Otros
        Este método tambien inicializa el atributo `puntaje` a un valor por defecto de 0.
        """

        if len(nombre) == 0:
            raise ValueError("El nombre de un jugador no puede ser vacío.")
        
        if ficha_actual not in ["X", "O"]:
            raise ValueError("La ficha no es un válida")
        
        self.puntaje : int = 0
        self.nombre :str = nombre
        self.ficha_actual : str = ficha_actual

    def estado(self)->None:
        """Muestra en la salida estándar los atributos de un Jugador."""

        print(f"Nombre: {self.nombre}")
        print(f"Ficha actual: {self.ficha_actual}")
        print(f"Puntaje actual: {self.puntaje}")

    def get_nombre(self)->str:
        """Retorna el nombre de un Jugador"""

        return self.nombre
    
    def set_nombre(self, nombre:str):
        """Modifica el nombre de un Jugador por el argumento `nombre`."""

        if len(nombre) == 0:
            raise ValueError("El valor del nombre no puede ser vacío")
        
        self.nombre = nombre
    
    def get_ficha_actual(self)->str:
        """Retorna la ficha actual de un Jugador"""

        return self.ficha_actual
    
    def set_ficha_actual(self, ficha_actual:str):
        """Modifica el valor de ficha_actual de un Jugador"""

        if ficha_actual not in ["X", "O"]:
            raise ValueError("El valor de ficha no es válido")
        
        self.ficha_actual=ficha_actual
    
    def get_puntaje(self)->int:
        """Retorna el puntaje actual de un Jugador"""

        return self.puntaje
    
    def set_puntaje(self, puntaje:int):
        """Modifica el puntaje de un Jugador"""

        try:
            puntaje = int(puntaje)
        except:
            raise TypeError("El puntaje no es entero")

        if puntaje < 0:
            raise ValueError("El puntaje debe ser no negativo")
        
        self.puntaje = puntaje


    def ganar_punto(self):
        """Incrementa `puntaje` en 1 unidad."""

        self.puntaje = self.puntaje + 1

    def cambiar_ficha(self):
        """Alterna el valor de `ficha_actual` por el otro en ["X", "O"]"""

        if self.ficha_actual == "X":
            self.ficha_actual = "O"
        else:
            self.ficha_actual = "X"
