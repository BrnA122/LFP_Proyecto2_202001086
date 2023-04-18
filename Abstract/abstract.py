from abc import ABC, abstractmethod

class Expression(ABC):

    def __init__(self, tipo, lexema, fila, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

    @abstractmethod
    def operar(self, arbol):
        pass

    @abstractmethod
    def getFila(self):
        return self.fila
    
    @abstractmethod
    def getColumna(self):
        return self.columna
    
    @abstractmethod
    def getTipo(self):
        return self.tipo
    
    @abstractmethod
    def getLexema(self):
        return self.lexema
    