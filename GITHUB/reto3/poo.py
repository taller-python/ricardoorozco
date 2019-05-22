"""Definicion de clases python - Compuertas"""
class Compuerta(object):

    def __init__(self, in_a, in_b):
        self.__in_a = in_a
        self.__in_b = in_b
        self.__out = 0

    def __init__(self):
        self.__in_a = 0
        self.__in_b = 0
        self.__out = 0

    def set_a(self, in_a):
        self.__in_a = in_a

    def set_b(self, in_b):
        self.__in_b = in_b

    def set_out(self, out):
        self.__out = out

    def get_a(self):
        return self.__in_a

    def get_b(self):
        return self.__in_b

    def get_out(self):
        return self.__out

class CompuertaOR(Compuerta):

    def __init__(self):
        Compuerta.__init__(self)

    def evaluar(self, signal_a, signal_b):
        Compuerta.set_a(self, signal_a)
        Compuerta.set_b(self, signal_b)
        Compuerta.set_out(self, 1 if Compuerta.get_a(self) or Compuerta.get_b(self) else 0)
        return Compuerta.get_out(self)

class CompuertaAND(Compuerta):
    def __init__(self):
        Compuerta.__init__(self)

    def evaluar(self, signal_a, signal_b):
        Compuerta.set_a(self, signal_a)
        Compuerta.set_b(self, signal_b)
        Compuerta.set_out(self, 1 if Compuerta.get_a(self) and Compuerta.get_b(self) else 0)
        return Compuerta.get_out(self)