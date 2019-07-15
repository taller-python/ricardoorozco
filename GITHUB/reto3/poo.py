"""Definicion de clases python - Compuertas"""
class Compuerta(object):
    "Clase generica para Compuertas logicas"
    def __init__(self, in_a, in_b):
        "Metodo inicializador de clase con parametros"
        self.__in_a = in_a
        self.__in_b = in_b
        self.__out = 0

    def set_a(self, in_a):
        "Metodo asignacion compuerta A"
        self.__in_a = in_a

    def set_b(self, in_b):
        "Metodo asignacion compuerta A"
        self.__in_b = in_b

    def set_out(self, out):
        "Metodo asignacion compuerta salida"
        self.__out = out

    def get_a(self):
        "Metodo obtencion compuerta A"
        return self.__in_a

    def get_b(self):
        "Metodo obtencion compuerta B"
        return self.__in_b

    def get_out(self):
        "Metodo obtencion compuerta salida"
        return self.__out

class CompuertaOR(Compuerta):
    "Clase para compuerta tipo OR"
    def __init__(self):
        "Metodo de inicializacion"
        Compuerta.__init__(self, 0, 0)

    def evaluar(self, signal_a, signal_b):
        "Metodo para evaluar logica de compuertas OR"
        Compuerta.set_a(self, signal_a)
        Compuerta.set_b(self, signal_b)
        Compuerta.set_out(self, 1 if Compuerta.get_a(self) or Compuerta.get_b(self) else 0)
        return Compuerta.get_out(self)

class CompuertaAND(Compuerta):
    "Clase para compuerta tipo OR"
    def __init__(self):
        "Metodo de inicializacion"
        Compuerta.__init__(self, 0, 0)

    def evaluar(self, signal_a, signal_b):
        "Metodo para evaluar logica de compuertas AND"
        Compuerta.set_a(self, signal_a)
        Compuerta.set_b(self, signal_b)
        Compuerta.set_out(self, 1 if Compuerta.get_a(self) and Compuerta.get_b(self) else 0)
        return Compuerta.get_out(self)
