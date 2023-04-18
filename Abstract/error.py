class Error():

    def __init__(self, tipo, lexema, fila, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

    def getLexema(self):
        return self.lexema
    
    def getTipo(self):
        return self.tipo
    
    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna