from Analizador.Analizador import *
from Abstract.lexema import *

class Sintactico():
    def __init__(self):
        self.err_sintac = []
        self.listaToken = []
        self.lista_datas = []
        self.error = False

    def analizar(self, listaToken):
        self.i = 0
        self.listaToken = listaToken
        self.analisis_sintactico()
        return self.lista_datas, self.err_sintac


    def analisis_sintactico(self):
        global comentarios
        while self.i<len(self.listaToken):
            if self.listaToken[self.i][1] == 'CrearBD':
                self.crearBD()
            elif self.listaToken[self.i][1] == 'EliminarBD':
                self.eliminarBD()
            elif self.listaToken[self.i][1] == 'CrearColeccion':
                self.crearColeccion()
            elif self.listaToken[self.i][1] == 'EliminarColeccion':
                self.eliminarColeccion()
            elif self.listaToken[self.i][1] == 'InsertarUnico':
                self.insertarUnico()
            elif self.listaToken[self.i][1] == 'ActualizarUnico':
                self.actualizarUnico()
            elif self.listaToken[self.i][1] == 'EliminarUnico':
                self.eliminarUnico()
            elif self.listaToken[self.i][1] == 'BuscarTodo':
                self.buscarTodo()
            elif self.listaToken[self.i][1] == 'BuscarUnico':
                self.buscarUnico()
            elif self.listaToken[self.i][0] in comentarios:
                self.i +=1
            else:
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                self.i+=1
                err = Lexema("Error Sintactico", "Se esperaba un Comando", err_lin, err_col)    
                self.err_sintac.append(err)
                break
        return None

    def crearBD(self):
        data = ''
        if self.listaToken[self.i][0] == 'RCREARBD':
            self.i += 1
            if self.listaToken[self.i][0] == 'RIDENTIFICADOR':
                id_bd = str(self.listaToken[self.i][1]).replace('\"', '')
                self.i += 1
                if self.listaToken[self.i][0] == 'IGUAL':
                    self.i += 1
                    if self.listaToken[self.i][0] == 'RPALABRARESERVADA':
                        self.i += 1
                        if self.listaToken[self.i][0] == 'RCREARBD':
                            self.i += 1
                            if self.listaToken[self.i][0] == 'PARENTESIS_IZ':
                                self.i += 1
                                if self.listaToken[self.i][0] == 'PARENTESIS_DE':
                                    self.i += 1
                                    if self.listaToken[self.i][0] == 'PUNTOYCOMA':
                                        self.i += 1
                                        data = f'use(\'{id_bd}\');'
                                        self.lista_datas.append(data)
                                    else:
                                        #self.i -= 1
                                        err_lin = self.listaToken[self.i][2]
                                        err_col = self.listaToken[self.i][3]
                                        err = Lexema("Error Sintactico", "Se esperaba un ;", err_lin, err_col)
                                        self.err_sintac.append(err)
                                        #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una ;")
                                else:
                                    #self.i -= 1
                                    err_lin = self.listaToken[self.i][2]
                                    err_col = self.listaToken[self.i][3]
                                    err = Lexema("Error Sintactico", "Se esperaba un )", err_lin, err_col)
                                    self.err_sintac.append(err)
                                    #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una )")
                            else:
                                #self.i -= 1
                                err_lin = self.listaToken[self.i][2]
                                err_col = self.listaToken[self.i][3]
                                err = Lexema("Error Sintactico", "Se esperaba un (", err_lin, err_col)
                                self.err_sintac.append(err)
                                #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una (")
                        else:
                            #self.i -= 1
                            err_lin = self.listaToken[self.i][2]
                            err_col = self.listaToken[self.i][3]
                            err = Lexema("Error Sintactico", "Se esperaba una CrearBD", err_lin, err_col)
                            self.err_sintac.append(err)
                            #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una CrearBD")
                    else:
                        #self.i -= 1
                        err_lin = self.listaToken[self.i][2]
                        err_col = self.listaToken[self.i][3]
                        err = Lexema("Error Sintactico", "Se esperaba Palabra Reservada", err_lin, err_col)
                        self.err_sintac.append(err)
                        #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba Palabra Reservada")
                else:
                    #self.i -= 1
                    err_lin = self.listaToken[self.i][2]
                    err_col = self.listaToken[self.i][3]
                    err = Lexema("Error Sintactico", "Se esperaba una Igual", err_lin, err_col)    
                    self.err_sintac.append(err)
                    #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una Igual")
            else:
                #self.i -= 1
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                err = Lexema("Error Sintactico", "Se esperaba una identificador", err_lin, err_col)    
                self.err_sintac.append(err)
                #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una identificador")
        else:
            err_lin = self.listaToken[self.i][2]
            err_col = self.listaToken[self.i][3]
            #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una CrearBD")

    def eliminarBD(self):
        data = ''
        if self.listaToken[self.i][0] == 'RELIMINARBD':
            self.i += 1
            if self.listaToken[self.i][0] == 'RIDENTIFICADOR':
                self.i += 1
                if self.listaToken[self.i][0] == 'IGUAL':
                    self.i += 1
                    if self.listaToken[self.i][0] == 'RPALABRARESERVADA':
                        self.i += 1
                        if self.listaToken[self.i][0] == 'RELIMINARBD':
                            self.i += 1
                            if self.listaToken[self.i][0] == 'PARENTESIS_IZ':
                                self.i += 1
                                if self.listaToken[self.i][0] == 'RATRIBUTO':
                                    self.i += 1
                                    if self.listaToken[self.i][0] == 'PARENTESIS_DE':
                                        self.i += 1
                                        if self.listaToken[self.i][0] == 'PUNTOYCOMA':
                                            self.i += 1
                                            data = f'db.dropDatabase();'
                                            self.lista_datas.append(data)
                                        else:
                                            #self.i -= 1
                                            err_lin = self.listaToken[self.i][2]
                                            err_col = self.listaToken[self.i][3]
                                            err = Lexema("Error Sintactico", "Se esperaba un ;", err_lin, err_col)
                                            self.err_sintac.append(err)
                                            #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una ;")
                                    else:
                                        #self.i -= 1
                                        err_lin = self.listaToken[self.i][2]
                                        err_col = self.listaToken[self.i][3]
                                        err = Lexema("Error Sintactico", "Se esperaba una )", err_lin, err_col)
                                        self.err_sintac.append(err)
                                        #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una )")
                                else:
                                    #self.i -= 1
                                    err_lin = self.listaToken[self.i][2]
                                    err_col = self.listaToken[self.i][3]
                                    err = Lexema("Error Sintactico", "Se esperaba una Atributo", err_lin, err_col)
                                    self.err_sintac.append(err)
                                    #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una Atributo")
                            else:
                                #self.i -= 1
                                err_lin = self.listaToken[self.i][2]
                                err_col = self.listaToken[self.i][3]
                                err = Lexema("Error Sintactico", "Se esperaba una (", err_lin, err_col)
                                self.err_sintac.append(err)
                                #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una (")
                        else:
                            #self.i -= 1
                            err_lin = self.listaToken[self.i][2]
                            err_col = self.listaToken[self.i][3]
                            err = Lexema("Error Sintactico", "Se esperaba una EliminarBD", err_lin, err_col)
                            self.err_sintac.append(err)
                            #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una EliminarBD")
                    else:
                        #self.i -= 1
                        err_lin = self.listaToken[self.i][2]
                        err_col = self.listaToken[self.i][3]
                        err = Lexema("Error Sintactico", "Se esperaba Palabra Reservada", err_lin, err_col)
                        self.err_sintac.append(err)
                        #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba Palabra Reservada")
                else:
                    #self.i -= 1
                    err_lin = self.listaToken[self.i][2]
                    err_col = self.listaToken[self.i][3]
                    err = Lexema("Error Sintactico", "Se esperaba una Igual", err_lin, err_col)
                    self.err_sintac.append(err)
                    #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una Igual")
            else:
                #self.i -= 1
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                err = Lexema("Error Sintactico", "Se esperaba una identificador", err_lin, err_col)
                self.err_sintac.append(err)
                #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una identificador",self.listaToken[self.i][0])
        else:
            err_lin = self.listaToken[self.i][2]
            err_col = self.listaToken[self.i][3]
            #print("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una EliminarBD")
    
    def crearColeccion(self):
        data = ''
        if self.listaToken[self.i][0] == 'RCREARCOLECCION':
            self.i += 1
            if self.listaToken[self.i][0] == 'RIDENTIFICADOR':
                self.i += 1
                if self.listaToken[self.i][0] == 'IGUAL':
                    self.i += 1
                    if self.listaToken[self.i][0] == 'RPALABRARESERVADA':
                        self.i += 1
                        if self.listaToken[self.i][0] == 'RCREARCOLECCION':
                            self.i += 1
                            if self.listaToken[self.i][0] == 'PARENTESIS_IZ':
                                self.i += 1
                                if self.listaToken[self.i][0] == 'RATRIBUTO':
                                    id_collec = str(self.listaToken[self.i][1]).replace('\"', '\'')
                                    self.i += 1
                                    if self.listaToken[self.i][0] == 'PARENTESIS_DE':
                                        self.i += 1
                                        if self.listaToken[self.i][0] == 'PUNTOYCOMA':
                                            self.i += 1
                                            data = f'db.createCollection({id_collec});'
                                            self.lista_datas.append(data)
                                        else:
                                            #self.i -= 1
                                            err_lin = self.listaToken[self.i][2]
                                            err_col = self.listaToken[self.i][3]
                                            err = Lexema("Error Sintactico", "Se esperaba una ;", err_lin, err_col)
                                            self.err_sintac.append(err)
                                    else:
                                        #self.i -= 1
                                        err_lin = self.listaToken[self.i][2]
                                        err_col = self.listaToken[self.i][3]
                                        err = Lexema("Error Sintactico", "Se esperaba una )", err_lin, err_col)
                                        self.err_sintac.append(err)
                                else:
                                    #self.i -= 1
                                    err_lin = self.listaToken[self.i][2]
                                    err_col = self.listaToken[self.i][3]
                                    err = Lexema("Error Sintactico", "Se esperaba una Atributo", err_lin, err_col)
                                    self.err_sintac.append(err)
                            else:
                                #self.i -= 1
                                err_lin = self.listaToken[self.i][2]
                                err_col = self.listaToken[self.i][3]
                                err = Lexema("Error Sintactico", "Se esperaba una (", err_lin, err_col)
                                self.err_sintac.append(err)
                        else:
                            #self.i -= 1
                            err_lin = self.listaToken[self.i][2]
                            err_col = self.listaToken[self.i][3]
                            err = Lexema("Error Sintactico", "Se esperaba una CrearColeccion", err_lin, err_col)
                            self.err_sintac.append(err)
                    else:
                        #self.i -= 1
                        err_lin = self.listaToken[self.i][2]
                        err_col = self.listaToken[self.i][3]
                        err = Lexema("Error Sintactico", "Se esperaba Palabra Reservada", err_lin, err_col)
                        self.err_sintac.append(err)
                else:
                    #self.i -= 1
                    err_lin = self.listaToken[self.i][2]
                    err_col = self.listaToken[self.i][3]
                    err = Lexema("Error Sintactico", "Se esperaba una Igual", err_lin, err_col)
                    self.err_sintac.append(err)
            else:
                #self.i -= 1
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                err = Lexema("Error Sintactico", "Se esperaba una identificador", err_lin, err_col)
                self.err_sintac.append(err)
        else:
            err_lin = self.listaToken[self.i][2]
            err_col = self.listaToken[self.i][3]
            #self.err_sintac.append("Error Sintactico", "Linea: ",err_lin, "Columna: ",err_col, "Se esperaba una CrearColeccion")

    def eliminarColeccion(self):
        data = ''
        if self.listaToken[self.i][0] == 'RELIMINARCOLECCION':
            self.i += 1
            if self.listaToken[self.i][0] == 'RIDENTIFICADOR':
                self.i += 1
                if self.listaToken[self.i][0] == 'IGUAL':
                    self.i += 1
                    if self.listaToken[self.i][0] == 'RPALABRARESERVADA':
                        self.i += 1
                        if self.listaToken[self.i][0] == 'RELIMINARCOLECCION':
                            self.i += 1
                            if self.listaToken[self.i][0] == 'PARENTESIS_IZ':
                                self.i += 1
                                if self.listaToken[self.i][0] == 'RATRIBUTO':
                                    id_collec = str(self.listaToken[self.i][1]).replace('\"', '')
                                    self.i += 1
                                    if self.listaToken[self.i][0] == 'PARENTESIS_DE':
                                        self.i += 1
                                        if self.listaToken[self.i][0] == 'PUNTOYCOMA':
                                            self.i += 1
                                            data = f'db.{id_collec}.drop();'
                                            self.lista_datas.append(data)
                                        else:
                                            #self.i -= 1
                                            err_lin = self.listaToken[self.i][2]
                                            err_col = self.listaToken[self.i][3]
                                            err = Lexema("Error Sintactico", "Se esperaba una ;", err_lin, err_col)
                                            self.err_sintac.append(err)
                                    else:
                                        #self.i -= 1
                                        err_lin = self.listaToken[self.i][2]
                                        err_col = self.listaToken[self.i][3]
                                        err = Lexema("Error Sintactico", "Se esperaba una )", err_lin, err_col)
                                        self.err_sintac.append(err)
                                else:
                                    #self.i -= 1
                                    err_lin = self.listaToken[self.i][2]
                                    err_col = self.listaToken[self.i][3]
                                    err = Lexema("Error Sintactico", "Se esperaba una Atributo", err_lin, err_col)
                                    self.err_sintac.append(err)
                            else:
                                #self.i -= 1
                                err_lin = self.listaToken[self.i][2]
                                err_col = self.listaToken[self.i][3]
                                err = Lexema("Error Sintactico", "Se esperaba una (", err_lin, err_col)
                                self.err_sintac.append(err)
                        else:
                            #self.i -= 1
                            err_lin = self.listaToken[self.i][2]
                            err_col = self.listaToken[self.i][3]
                            err = Lexema("Error Sintactico", "Se esperaba una EliminarColeccion", err_lin, err_col)
                            self.err_sintac.append(err)
                    else:
                        #self.i -= 1
                        err_lin = self.listaToken[self.i][2]
                        err_col = self.listaToken[self.i][3]
                        err = Lexema("Error Sintactico", "Se esperaba Palabra Reservada", err_lin, err_col)
                        self.err_sintac.append(err)
                else:
                    #self.i -= 1
                    err_lin = self.listaToken[self.i][2]
                    err_col = self.listaToken[self.i][3]
                    err = Lexema("Error Sintactico", "Se esperaba una Igual", err_lin, err_col)
                    self.err_sintac.append(err)
            else:
                #self.i -= 1
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                err = Lexema("Error Sintactico", "Se esperaba una identificador", err_lin, err_col)
                self.err_sintac.append(err)
        else:
            err_lin = self.listaToken[self.i][2]
            err_col = self.listaToken[self.i][3]


    def insertarUnico(self):
        data = ''
        if self.listaToken[self.i][0] == 'RINSERTAR':
            self.i += 1
            if self.listaToken[self.i][0] == 'RIDENTIFICADOR':
                self.i += 1
                if self.listaToken[self.i][0] == 'IGUAL':
                    self.i += 1
                    if self.listaToken[self.i][0] == 'RPALABRARESERVADA':
                        self.i += 1
                        if self.listaToken[self.i][0] == 'RINSERTAR':
                            self.i += 1
                            if self.listaToken[self.i][0] == 'PARENTESIS_IZ':
                                self.i += 1
                                if self.listaToken[self.i][0] == 'RATRIBUTO':
                                    id_collec = str(self.listaToken[self.i][1]).replace('\"', '')
                                    self.i += 1
                                    if self.listaToken[self.i][0] == 'COMA':
                                        self.i += 1
                                        if self.listaToken[self.i][0] == 'RJSON':
                                            archivo = str(self.listaToken[self.i][1]).strip('"').replace('\\n', '\n')
                                            self.i += 1
                                            if self.listaToken[self.i][0] == 'PARENTESIS_DE':
                                                self.i += 1
                                                if self.listaToken[self.i][0] == 'PUNTOYCOMA':
                                                    self.i += 1
                                                    data = f'db.{id_collec}.insertOne({archivo});'
                                                    self.lista_datas.append(data)
                                                else:
                                                    #self.i -= 1
                                                    err_lin = self.listaToken[self.i][2]
                                                    err_col = self.listaToken[self.i][3]
                                                    err = Lexema("Error Sintactico", "Se esperaba una ;", err_lin, err_col)
                                                    self.err_sintac.append(err)
                                            else:
                                                #self.i -= 1
                                                err_lin = self.listaToken[self.i][2]
                                                err_col = self.listaToken[self.i][3]
                                                err = Lexema("Error Sintactico", "Se esperaba una )", err_lin, err_col)
                                                self.err_sintac.append(err)
                                        else:
                                            #self.i -= 1
                                            err_lin = self.listaToken[self.i][2]
                                            err_col = self.listaToken[self.i][3]
                                            err = Lexema("Error Sintactico", "Se esperaba una JSON", err_lin, err_col)
                                            self.err_sintac.append(err)
                                    else:
                                        #self.i -= 1
                                        err_lin = self.listaToken[self.i][2]
                                        err_col = self.listaToken[self.i][3]
                                        err = Lexema("Error Sintactico", "Se esperaba una ,", err_lin, err_col)
                                        self.err_sintac.append(err)
                                else:
                                    #self.i -= 1
                                    err_lin = self.listaToken[self.i][2]
                                    err_col = self.listaToken[self.i][3]
                                    err = Lexema("Error Sintactico", "Se esperaba una Atributo", err_lin, err_col)
                                    self.err_sintac.append(err)
                            else:
                                #self.i -= 1
                                err_lin = self.listaToken[self.i][2]
                                err_col = self.listaToken[self.i][3]
                                err = Lexema("Error Sintactico", "Se esperaba una (", err_lin, err_col)
                                self.err_sintac.append(err)
                        else:
                            #self.i -= 1
                            err_lin = self.listaToken[self.i][2]
                            err_col = self.listaToken[self.i][3]
                            err = Lexema("Error Sintactico", "Se esperaba una InsertarUnico", err_lin, err_col)
                            self.err_sintac.append(err)
                    else:
                        #self.i -= 1
                        err_lin = self.listaToken[self.i][2]
                        err_col = self.listaToken[self.i][3]
                        err = Lexema("Error Sintactico", "Se esperaba una Palabra Reservada", err_lin, err_col)
                        self.err_sintac.append(err)
                else:
                    #self.i -= 1
                    err_lin = self.listaToken[self.i][2]
                    err_col = self.listaToken[self.i][3]
                    err = Lexema("Error Sintactico", "Se esperaba un Igual", err_lin, err_col)
                    self.err_sintac.append(err)
            else:
                #self.i -= 1
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                err = Lexema("Error Sintactico", "Se esperaba un identificador", err_lin, err_col)
                self.err_sintac.append(err)
        else:
            err_lin = self.listaToken[self.i][2]
            err_col = self.listaToken[self.i][3]
            err = Lexema("Error Sintactico", "Se esperaba un identificador", err_lin, err_col)
            self.err_sintac.append(err)


    def actualizarUnico(self):
        data = ''
        if self.listaToken[self.i][0] == 'RACTUALIZARUNICO':
            self.i += 1
            if self.listaToken[self.i][0] == 'RIDENTIFICADOR':
                self.i += 1
                if self.listaToken[self.i][0] == 'IGUAL':
                    self.i += 1
                    if self.listaToken[self.i][0] == 'RPALABRARESERVADA':
                        self.i += 1
                        if self.listaToken[self.i][0] == 'RACTUALIZARUNICO':
                            self.i += 1
                            if self.listaToken[self.i][0] == 'PARENTESIS_IZ':
                                self.i += 1
                                if self.listaToken[self.i][0] == 'RATRIBUTO':
                                    id_collec = str(self.listaToken[self.i][1]).replace('\"', '')
                                    self.i += 1
                                    if self.listaToken[self.i][0] == 'COMA':
                                        self.i += 1
                                        if self.listaToken[self.i][0] == 'RJSON':
                                            archivo1 = str(self.listaToken[self.i][1]).strip('"').replace('\\n', '\n')
                                            self.i += 1
                                            if self.listaToken[self.i][0] == 'COMA':
                                                self.i += 1
                                                if self.listaToken[self.i][0] == 'RJSON':
                                                    archivo2 = str(self.listaToken[self.i][1]).strip('"').replace('\\n', '\n')
                                                    self.i += 1
                                                    if self.listaToken[self.i][0] == 'PARENTESIS_DE':
                                                        self.i += 1
                                                        if self.listaToken[self.i][0] == 'PUNTOYCOMA':
                                                            self.i += 1
                                                            data = f'db.{id_collec}.updateOne({archivo1}, {archivo2});'
                                                            self.lista_datas.append(data)
                                                        else:
                                                            #self.i -= 1
                                                            err_lin = self.listaToken[self.i][2]
                                                            err_col = self.listaToken[self.i][3]
                                                            err = Lexema("Error Sintactico", "Se esperaba una ;", err_lin, err_col)
                                                            self.err_sintac.append(err)
                                                    else:
                                                        #self.i -= 1
                                                        err_lin = self.listaToken[self.i][2]
                                                        err_col = self.listaToken[self.i][3]
                                                        err = Lexema("Error Sintactico", "Se esperaba una )", err_lin, err_col)
                                                        self.err_sintac.append(err)
                                                else:
                                                    #self.i -= 1
                                                    err_lin = self.listaToken[self.i][2]
                                                    err_col = self.listaToken[self.i][3]
                                                    err = Lexema("Error Sintactico", "Se esperaba una JSON", err_lin, err_col)
                                                    self.err_sintac.append(err)
                                            else:
                                                #self.i -= 1
                                                err_lin = self.listaToken[self.i][2]
                                                err_col = self.listaToken[self.i][3]
                                                err = Lexema("Error Sintactico", "Se esperaba una ,", err_lin, err_col)
                                                self.err_sintac.append(err)
                                        else:
                                            #self.i -= 1
                                            err_lin = self.listaToken[self.i][2]
                                            err_col = self.listaToken[self.i][3]
                                            err = Lexema("Error Sintactico", "Se esperaba una JSON", err_lin, err_col)
                                            self.err_sintac.append(err)
                                    else:
                                        #self.i -= 1
                                        err_lin = self.listaToken[self.i][2]
                                        err_col = self.listaToken[self.i][3]
                                        err = Lexema("Error Sintactico", "Se esperaba una ,", err_lin, err_col)
                                        self.err_sintac.append(err)
                                else:
                                    #self.i -= 1
                                    err_lin = self.listaToken[self.i][2]
                                    err_col = self.listaToken[self.i][3]
                                    err = Lexema("Error Sintactico", "Se esperaba una Atributo", err_lin, err_col)
                                    self.err_sintac.append(err)
                            else:
                                #self.i -= 1
                                err_lin = self.listaToken[self.i][2]
                                err_col = self.listaToken[self.i][3]
                                err = Lexema("Error Sintactico", "Se esperaba una (", err_lin, err_col)
                                self.err_sintac.append(err)
                        else:
                            #self.i -= 1
                            err_lin = self.listaToken[self.i][2]
                            err_col = self.listaToken[self.i][3]
                            err = Lexema("Error Sintactico", "Se esperaba una ActualizarUnico", err_lin, err_col)
                            self.err_sintac.append(err)
                    else:
                        #self.i -= 1
                        err_lin = self.listaToken[self.i][2]
                        err_col = self.listaToken[self.i][3]
                        err = Lexema("Error Sintactico", "Se esperaba una Palabra Reservada", err_lin, err_col)
                        self.err_sintac.append(err)
                else:
                    #self.i -= 1
                    err_lin = self.listaToken[self.i][2]
                    err_col = self.listaToken[self.i][3]
                    err = Lexema("Error Sintactico", "Se esperaba un Igual", err_lin, err_col)
                    self.err_sintac.append(err)
            else:
                #self.i -= 1
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                err = Lexema("Error Sintactico", "Se esperaba un identificador", err_lin, err_col)
                self.err_sintac.append(err)
        else:
            err_lin = self.listaToken[self.i][2]
            err_col = self.listaToken[self.i][3]

    def eliminarUnico(self):
        data = ''
        if self.listaToken[self.i][0] == 'RELIMINARUNICO':
            self.i += 1
            if self.listaToken[self.i][0] == 'RIDENTIFICADOR':
                self.i += 1
                if self.listaToken[self.i][0] == 'IGUAL':
                    self.i += 1
                    if self.listaToken[self.i][0] == 'RPALABRARESERVADA':
                        self.i += 1
                        if self.listaToken[self.i][0] == 'RELIMINARUNICO':
                            self.i += 1
                            if self.listaToken[self.i][0] == 'PARENTESIS_IZ':
                                self.i += 1
                                if self.listaToken[self.i][0] == 'RATRIBUTO':
                                    id_collec = str(self.listaToken[self.i][1]).replace('\"', '')
                                    self.i += 1
                                    if self.listaToken[self.i][0] == 'COMA':
                                        self.i += 1
                                        if self.listaToken[self.i][0] == 'RJSON':
                                            archivo = str(self.listaToken[self.i][1]).strip('"').replace('\\n', '\n')
                                            self.i += 1
                                            if self.listaToken[self.i][0] == 'PARENTESIS_DE':
                                                self.i += 1
                                                if self.listaToken[self.i][0] == 'PUNTOYCOMA':
                                                    self.i += 1
                                                    data = f'db.{id_collec}.deleteOne({archivo});'
                                                    self.lista_datas.append(data)
                                                else:
                                                    #self.i -= 1
                                                    err_lin = self.listaToken[self.i][2]
                                                    err_col = self.listaToken[self.i][3]
                                                    err = Lexema("Error Sintactico", "Se esperaba una ;", err_lin, err_col)
                                                    self.err_sintac.append(err)
                                            else:
                                                #self.i -= 1
                                                err_lin = self.listaToken[self.i][2]
                                                err_col = self.listaToken[self.i][3]
                                                err = Lexema("Error Sintactico", "Se esperaba una )", err_lin, err_col)
                                                self.err_sintac.append(err)
                                        else:       
                                            #self.i -= 1
                                            err_lin = self.listaToken[self.i][2]
                                            err_col = self.listaToken[self.i][3]
                                            err = Lexema("Error Sintactico", "Se esperaba una JSON", err_lin, err_col)
                                            self.err_sintac.append(err)
                                    else:
                                        #self.i -= 1
                                        err_lin = self.listaToken[self.i][2]
                                        err_col = self.listaToken[self.i][3]
                                        err = Lexema("Error Sintactico", "Se esperaba una ,", err_lin, err_col)
                                        self.err_sintac.append(err)
                                else:
                                    #self.i -= 1
                                    err_lin = self.listaToken[self.i][2]
                                    err_col = self.listaToken[self.i][3]
                                    err = Lexema("Error Sintactico", "Se esperaba una Atributo", err_lin, err_col)
                                    self.err_sintac.append(err)
                            else:
                                #self.i -= 1
                                err_lin = self.listaToken[self.i][2]
                                err_col = self.listaToken[self.i][3]
                                err = Lexema("Error Sintactico", "Se esperaba una (", err_lin, err_col)
                                self.err_sintac.append(err)
                        else:
                            #self.i -= 1
                            err_lin = self.listaToken[self.i][2]
                            err_col = self.listaToken[self.i][3]
                            err = Lexema("Error Sintactico", "Se esperaba una EliminarUnico", err_lin, err_col)
                            self.err_sintac.append(err)
                    else:
                        #self.i -= 1
                        err_lin = self.listaToken[self.i][2]
                        err_col = self.listaToken[self.i][3]
                        err = Lexema("Error Sintactico", "Se esperaba una Palabra Reservada", err_lin, err_col)
                        self.err_sintac.append(err)
                else:
                    #self.i -= 1
                    err_lin = self.listaToken[self.i][2]
                    err_col = self.listaToken[self.i][3]
                    err = Lexema("Error Sintactico", "Se esperaba un Igual", err_lin, err_col)
                    self.err_sintac.append(err)
            else:
                #self.i -= 1
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                err = Lexema("Error Sintactico", "Se esperaba un identificador", err_lin, err_col)
                self.err_sintac.append(err)
        else:
            err_lin = self.listaToken[self.i][2]
            err_col = self.listaToken[self.i][3]

            

    def buscarTodo(self):
        data = ''
        if self.listaToken[self.i][0] == 'RBUSCARTODO':
            self.i += 1
            if self.listaToken[self.i][0] == 'RIDENTIFICADOR':
                self.i += 1
                if self.listaToken[self.i][0] == 'IGUAL':
                    self.i += 1
                    if self.listaToken[self.i][0] == 'RPALABRARESERVADA':
                        self.i += 1
                        if self.listaToken[self.i][0] == 'RBUSCARTODO':
                            self.i += 1
                            if self.listaToken[self.i][0] == 'PARENTESIS_IZ':
                                self.i += 1
                                if self.listaToken[self.i][0] == 'RATRIBUTO':
                                    id_collec = str(self.listaToken[self.i][1]).replace('\"', '')
                                    self.i += 1
                                    if self.listaToken[self.i][0] == 'PARENTESIS_DE':
                                        self.i += 1
                                        if self.listaToken[self.i][0] == 'PUNTOYCOMA':
                                            self.i += 1
                                            data = f'db.{id_collec}.find();'
                                            self.lista_datas.append(data)
                                        else:
                                            #self.i -= 1
                                            err_lin = self.listaToken[self.i][2]
                                            err_col = self.listaToken[self.i][3]
                                            err = Lexema("Error Sintactico", "Se esperaba una ;", err_lin, err_col)
                                            self.err_sintac.append(err)
                                    else:
                                        #self.i -= 1
                                        err_lin = self.listaToken[self.i][2]
                                        err_col = self.listaToken[self.i][3]
                                        err = Lexema("Error Sintactico", "Se esperaba una )", err_lin, err_col)
                                        self.err_sintac.append(err)
                                else:
                                    #self.i -= 1
                                    err_lin = self.listaToken[self.i][2]
                                    err_col = self.listaToken[self.i][3]
                                    err = Lexema("Error Sintactico", "Se esperaba una Atributo", err_lin, err_col)
                                    self.err_sintac.append(err)
                            else:
                                #self.i -= 1
                                err_lin = self.listaToken[self.i][2]
                                err_col = self.listaToken[self.i][3]
                                err = Lexema("Error Sintactico", "Se esperaba una (", err_lin, err_col)
                                self.err_sintac.append(err)
                        else:
                            #self.i -= 1
                            err_lin = self.listaToken[self.i][2]
                            err_col = self.listaToken[self.i][3]
                            err = Lexema("Error Sintactico", "Se esperaba una BuscarTodo", err_lin, err_col)
                            self.err_sintac.append(err)
                    else:
                        #self.i -= 1
                        err_lin = self.listaToken[self.i][2]
                        err_col = self.listaToken[self.i][3]
                        err = Lexema("Error Sintactico", "Se esperaba una Palabra Reservada", err_lin, err_col)
                        self.err_sintac.append(err)
                else:
                    #self.i -= 1
                    err_lin = self.listaToken[self.i][2]
                    err_col = self.listaToken[self.i][3]
                    err = Lexema("Error Sintactico", "Se esperaba un Igual", err_lin, err_col)
                    self.err_sintac.append(err)
            else:
                #self.i -= 1
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                err = Lexema("Error Sintactico", "Se esperaba un identificador", err_lin, err_col)
                self.err_sintac.append(err)
        else:
            err_lin = self.listaToken[self.i][2]
            err_col = self.listaToken[self.i][3]


    def buscarUnico(self):
        data = ''
        if self.listaToken[self.i][0] == 'RBUSCARUNICO':
            self.i += 1
            if self.listaToken[self.i][0] == 'RIDENTIFICADOR':
                self.i += 1
                if self.listaToken[self.i][0] == 'IGUAL':
                    self.i += 1
                    if self.listaToken[self.i][0] == 'RPALABRARESERVADA':
                        self.i += 1
                        if self.listaToken[self.i][0] == 'RBUSCARUNICO':
                            self.i += 1
                            if self.listaToken[self.i][0] == 'PARENTESIS_IZ':
                                self.i += 1
                                if self.listaToken[self.i][0] == 'RATRIBUTO':
                                    id_collec = str(self.listaToken[self.i][1]).replace('\"', '')
                                    self.i += 1
                                    if self.listaToken[self.i][0] == 'PARENTESIS_DE':
                                        self.i += 1
                                        if self.listaToken[self.i][0] == 'PUNTOYCOMA':
                                            self.i += 1
                                            data = f'db.{id_collec}.findOne();'
                                            self.lista_datas.append(data)
                                        else:
                                            #self.i -= 1
                                            err_lin = self.listaToken[self.i][2]
                                            err_col = self.listaToken[self.i][3]
                                            err = Lexema("Error Sintactico", "Se esperaba una ;", err_lin, err_col)
                                            self.err_sintac.append(err)
                                    else:
                                        #self.i -= 1
                                        err_lin = self.listaToken[self.i][2]
                                        err_col = self.listaToken[self.i][3]
                                        err = Lexema("Error Sintactico", "Se esperaba una )", err_lin, err_col)
                                        self.err_sintac.append(err)
                                else:
                                    #self.i -= 1
                                    err_lin = self.listaToken[self.i][2]
                                    err_col = self.listaToken[self.i][3]
                                    err = Lexema("Error Sintactico", "Se esperaba una Atributo", err_lin, err_col)
                                    self.err_sintac.append(err)
                            else:
                                #self.i -= 1
                                err_lin = self.listaToken[self.i][2]
                                err_col = self.listaToken[self.i][3]
                                err = Lexema("Error Sintactico", "Se esperaba una (", err_lin, err_col)
                                self.err_sintac.append(err)
                        else:
                            #self.i -= 1
                            err_lin = self.listaToken[self.i][2]
                            err_col = self.listaToken[self.i][3]
                            err = Lexema("Error Sintactico", "Se esperaba una BuscarUnico", err_lin, err_col)
                            self.err_sintac.append(err)
                    else:
                        #self.i -= 1
                        err_lin = self.listaToken[self.i][2]
                        err_col = self.listaToken[self.i][3]
                        err = Lexema("Error Sintactico", "Se esperaba una Palabra Reservada", err_lin, err_col)
                        self.err_sintac.append(err)
                else:
                    #self.i -= 1
                    err_lin = self.listaToken[self.i][2]
                    err_col = self.listaToken[self.i][3]
                    err = Lexema("Error Sintactico", "Se esperaba un Igual", err_lin, err_col)
                    self.err_sintac.append(err)
            else:
                #self.i -= 1
                err_lin = self.listaToken[self.i][2]
                err_col = self.listaToken[self.i][3]
                err = Lexema("Error Sintactico", "Se esperaba un identificador", err_lin, err_col)
                self.err_sintac.append(err)
        else:
            err_lin = self.listaToken[self.i][2]
            err_col = self.listaToken[self.i][3]




