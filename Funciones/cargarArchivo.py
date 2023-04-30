from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
import os


def Nuevo(entrada):
    global archivo_abierto
    seleccion = messagebox.askquestion(message="¿Desea guardar los cambios?", title="Nuevo")
    if seleccion == "yes":
        filename = fd.asksaveasfile(mode='w', defaultextension=".txt")
        if filename is None:
            return
        guardar = str(entrada.get(1.0, END)) 
        filename.write(guardar)
        filename.close()
    entrada.delete(1.0, END)
    archivo_abierto=None


def Abrir(entrada):
    global archivo_abierto
    
    
    actual = str(entrada.get(1.0, END)).strip()
    
    if len(actual) != 0:
        seleccion = messagebox.askquestion(message="¿Desea guardar los cambios?", title="Abrir")
        if seleccion == "yes":
            if archivo_abierto != None:
                open(archivo_abierto, "w", encoding= "utf-8").close()
                filename = open(archivo_abierto, "w", encoding= "utf-8")
                guardar = str(entrada.get(1.0, END)) 
                filename.write(guardar)
                filename.close()
            else:
                filename = fd.asksaveasfile(mode='w', defaultextension=".txt")
                if filename != None:
                    guardar = str(entrada.get(1.0, END)) 
                    filename.write(guardar)
                    filename.close()
                    
        entrada.delete(1.0, END)

    filename = fd.askopenfilename(filetypes=[("TXT files",".txt")])
    if filename == "":
        return
    archivo_abierto = filename
    file = open(filename,"r", encoding= "utf-8")
    readFile = file.read()
    file.close()
    entrada.insert(END, readFile)


def Guardar(entrada):
    if archivo_abierto != None:
        open(archivo_abierto, "w").close()
        filename = open(archivo_abierto, "w", encoding= "utf-8")
        guardar = str(entrada.get(1.0, END)) 
        filename.write(guardar)
        filename.close()
        messagebox.showinfo(message="Se han guardado los cambios", title="Guardar")
    else:
        messagebox.showwarning(message="No se ha seleccionado archivo de guardado", title="Guardar")
        GuardarComo(entrada)


def GuardarComo(entrada):
    filename=fd.asksaveasfilename(title = "Guardar como", defaultextension=".txt" ,filetypes = (("TXT files","*.txt"),("todos los archivos","*.*")))
    if filename is None:
        return
    guardar = str(entrada.get(1.0, END))
    archi1=open(filename, "w", encoding="utf-8")
    archi1.write(guardar)
    archi1.close()

def GuardarResultados(salida):
    data = ''
    namefile = os.path.basename(archivo_abierto) 

    for res in salida:
        data += str(res)+"\n"
    # Aqui creamos el archivo
    with open(namefile, 'w', encoding="utf-8") as f:
        f.write(data)