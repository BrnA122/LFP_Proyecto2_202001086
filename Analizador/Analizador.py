from tkinter import messagebox as mb
from Abstract.lexema import *

global lista_lexemas
global error_lexemas
global reconocidos

tokens_global = []
lista_lexemas = []
error_lexemas= []
lista_tokens = []

caracters = " \r"

def armar_comentario(lexema):
    estado = 0
    valido = [3]
    
    for char in lexema:
        if estado == 0:
            if char == "-":
                estado = 1
            else:
                estado = -5
        if estado == 1:
            if char == "-":
                estado = 2
            else:
                estado = -5
        elif estado == 2:
            if char == "-":
                estado = 3
            else:
                estado = -5
        elif estado == 3:
            if char != "\n":
                estado = 3
            else:
                estado = -5
                
    if estado in valido:
        return True
    else:
        return False
    
def armar_multilinea(lexema):
    estado = 0
    valido = [4]

    for char in lexema:   
        if estado == 0:
            if char == "/":
                estado = 1
            else:
                estado = -5
        elif estado == 1:
            if char == "*":
                estado = 2
            else:
                estado = -5
        elif estado == 2:
            if char == "*":
                estado = 3
            elif char == "\n" or char != "\n" :
                estado = 2
            else:
                estado = -5
        elif estado == 3:
            if char == "/":
                estado = 4
            else:
                estado = -5
        elif estado == 4:
            if char == "/" or char != "/":
                estado = -5

    if estado in valido:
        return True
    else:
        return False
    
def armar_palabra(lexema):
    estado = 0
    valido = [1]

    for char in lexema:
        if estado == 0:
            if char.isalpha():
                estado = 1
            else:
                estado = -5
        elif estado == 1:
            if char.isalpha() or char.isdigit():
                estado = 1
            else:
                estado = -5

    if estado in valido:
        return True
    else:
        return False

def armar_variable(lexema):
    estado = 0
    valido = [2]

    for char in lexema:
        if estado == 0:
            if char == '\"':
                estado = 1
            else:
                estado = -5
        elif estado == 1:
            if char == '\"':
                estado = 2
            elif char != '\n':
                estado = 1
            else:
                estado = -5
        elif estado == 2:
            if char == '\n' or char != '\n':
                estado = -5

    if estado in valido:
        return True
    else:
        return False  

def armar_json(lexema):
    estado = 0
    valido = [4]

    for char in lexema:   
        if estado == 0:
            if char == "\"":
                estado = 1
            else:
                estado = -5
        elif estado == 1:
            if char == "{":
                estado = 2
            else:
                estado = -5
        elif estado == 2:
            if char == "}":
                estado = 3
            elif char == "\n" or char != "\n":
                estado = 2
            else:
                estado = -5
        elif estado == 3:
            if char == "}":
                estado = 4
            elif char == "\"" :
                estado = 4
            else:
                estado = -5
        elif estado == 4:
            if char == "}":
                estado = -5
            elif char == "\"":
                estado = 4
            else:
                estado = -5

    if estado in valido:
        return True
    else:
        return False


#--------------Tokens-------------------------
global comentarios
tokens ={
    'RCREARBD'           : 'CrearBD',
    'RELIMINARBD'        : 'EliminarBD',
    'RCREARCOLECCION'    : 'CrearColeccion',
    'RELIMINARCOLECCION' : 'EliminarColeccion',
    'RINSERTAR'          : 'InsertarUnico',
    'RACTUALIZARUNICO'   : 'ActualizarUnico',
    'RELIMINARUNICO'     : 'EliminarUnico',
    'RBUSCARTODO'        : 'BuscarTodo',
    'RBUSCARUNICO'       : 'BuscarUnico',
    'RSETEAR'            : '$set',
    'RPALABRARESERVADA'  : 'nueva',
    "RATRIBUTO"          : armar_variable,
    'RIDENTIFICADOR'     : armar_palabra,
    'RJSON'              : armar_json,
    'RCOMENTARIO'        : armar_comentario,
    'RMULTILINEA'        : armar_multilinea,
    'DOSPUNTOS'          : ':',
    'PUNTOYCOMA'         : ';',
    'COMA'               : ',',
    'IGUAL'              : '=',
    'PARENTESIS_IZ'      : '(',
    'PARENTESIS_DE'      : ')',
    }

comentarios = ["RCOMENTARIO","RMULTILINEA"]

def instruccion(cadena):
    global lista_tokens
    global error_lexemas
    n_lin = 1
    n_col = 0
    puntero = 0
    error = False
    
    while puntero < len(cadena):
        char = cadena[puntero]
        reconocido = False
        n_col+=1

        if char == "\n":
            n_lin +=1
            n_col = 0
        
        elif char in caracters:
            puntero += 1
            n_col += 1
            continue
        
        for token, patron in tokens.items():
            if type(patron) == str:
                if puntero + len(patron) > len(cadena): continue

                lexema = cadena[puntero : puntero + len(patron)]
                
                if lexema == patron:
                    reconocido = True
                    lista_tokens.append((token,lexema,n_lin ,n_col))
                    l = Lexema(token, lexema, n_lin , n_col)
                    lista_lexemas.append(l)
                    puntero += len(patron)
                    n_col += len(patron)-1
                    break

            else:
                siguiente = puntero
                anterior = False

                while siguiente <= len(cadena):
                    lexema = cadena[puntero : siguiente]
                    reconocido = patron(lexema)

                    if not reconocido and anterior:
                        lexema = cadena[puntero : siguiente - 1]
                        reconocido = patron(lexema)
                        puntero = siguiente - 1
                        break  

                    anterior = reconocido
                    siguiente += 1

                if reconocido:
                    if "\n" in lexema:
                        for char in lexema:
                            n_col +=1
                            if char == "\n":
                                n_lin  +=1
                                n_col = 0
                    else:
                        n_col += siguiente - puntero -1

                    lexema = lexema.replace("\n","\\n")
                    lista_tokens.append((token,lexema,n_lin ,n_col))
                    l = Lexema(token, lexema, n_lin , n_col)
                    lista_lexemas.append(l)
                    puntero = siguiente - 1

            if reconocido: break

        if not reconocido:
            lexema = cadena[puntero]
            puntero += 1
            if lexema != '\n':
                err = Lexema("Error Lexico", lexema, n_lin, n_col)
                error_lexemas.append(err)
            error = True
        
    return lista_lexemas, error_lexemas
