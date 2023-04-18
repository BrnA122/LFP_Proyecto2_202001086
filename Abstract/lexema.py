from Abstract.abstract import Expression

class Lexema(Expression):

    def __init__(self, tipo, lexema, fila, columna):
        super().__init__(tipo, lexema, fila, columna)

    def operar(self, arbol):
        return self.tipo

    def getColumna(self):
        return super().getColumna()
    
    def getFila(self):
        return super().getFila()
    
    def getTipo(self):
        return super().getTipo()
    
    def getLexema(self):
        return super().getLexema()
    

    