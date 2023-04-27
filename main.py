import os
from tkinter import *
from tkinter import messagebox as mb
from tkinter import font
from tkinter import ttk
from Funciones.cargarArchivo import *
from Analizador.Analizador import *


class Inicio():
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("INICIO")
        ancho_ventana = 1250
        alto_ventana = 658
        x_ventana = self.ventana.winfo_screenwidth() 
        y_ventana = self.ventana.winfo_screenheight() 
        global analizador_sintac
        analizador_sintac = Sintactico()

        pwidth = round(x_ventana/2-ancho_ventana/2)
        pheight = round(y_ventana/2-alto_ventana/2-45)

        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(pwidth) + "+" + str(pheight)
        self.ventana.geometry(posicion)

                 #Cambiando el tipo de fuente
        self.defaultFont = font.nametofont("TkDefaultFont")      
        self.defaultFont.configure(family='Comic Sans MS', 
                                   size=12, 
                                   weight=font.BOLD)

        barra_menus = Menu()
        # Crear el primer menú.
        menu_archivo = Menu(barra_menus, tearoff=False)
        menu_ayuda = Menu(barra_menus, tearoff=False)
        menu_archivo.add_command(label="Nueva", command=lambda: self.manejoOpciones(1))
        menu_archivo.add_command(label="Abrir", command=lambda: self.manejoOpciones(2))
        menu_archivo.add_command(label="Guardar", command=lambda: self.manejoOpciones(3))
        menu_archivo.add_command(label="Guardar Como", command= lambda: self.manejoOpciones(4))
        menu_archivo.add_command(label="Salir", command=self.ventana.destroy)
        menu_ayuda.add_command(label="Manual de Usuario", command=lambda: self.manejoOpciones(5))
        menu_ayuda.add_command(label="Manual Técnico", command=lambda: self.manejoOpciones(6))
        menu_ayuda.add_command(label="Temas de Ayuda",command=lambda: self.manejoOpciones(7))
        # Agregarlo a la barra.
        barra_menus.add_cascade(menu=menu_archivo, label="Archivo")
        barra_menus.add_cascade(menu=menu_ayuda, label="Ayuda")
        
        Label(self.ventana, text="TEXTO DE ENTRADA", bg="CadetBlue4").place(x= 50, y = 170)
        self.txtArea = Text(self.ventana, borderwidth=3, relief="groove", wrap='none')
        self.txtArea.configure(font=('Comic Sans MS', 12,))
        self.txtArea.place(x = 50, y =200, width=550, height= 400)

        vscroll = Scrollbar(self.txtArea, orient= VERTICAL, command=self.txtArea.yview)
        self.txtArea['yscroll'] = vscroll.set
        vscroll.pack(side=RIGHT, fill="y")

        Label(self.ventana, text="SALIDA", bg="CadetBlue4").place(x= 650, y = 170)
        self.txtArea2 = Text(self.ventana, borderwidth=3, relief="groove")
        self.txtArea2.configure(font=('Comic Sans MS', 12,))
        self.txtArea2.place(x = 650, y =200, width=550, height= 400)
        vscroll2 = Scrollbar(self.txtArea2, orient= VERTICAL, command=self.txtArea2.yview)
        self.txtArea2['yscroll'] = vscroll2.set
        vscroll2.pack(side=RIGHT, fill="y")

        Label(self.ventana).place(x= 250, y= 638, height=20, width=1000)
        self.position_label = Label(
        self.ventana, text="Fila: 0 Columna: 0", anchor="w")
        self.position_label.place(x=0, y= 638, height=20, width=250)

        button_Analizar = Button(self.ventana, text="Analizar", command =lambda: self.Analizar()).place(x = 50, y=80, width=200, height=35)
        button_Tokens = Button(self.ventana, text="Ver Tokens", command =verTokens).place(x = 250, y=80, width=200, height=35)
        button_Errores = Button(self.ventana, text="Ver Errores", command =verErrores).place(x = 450, y=80, width=200, height=35)

        self.txtArea.bind("<KeyRelease>", self.refresh_position)

        self.ventana.config(menu=barra_menus)  
        self.ventana.configure(bg="CadetBlue4")
        self.ventana.resizable(0,0)
        self.ventana.mainloop()

    def refresh_position(self, event) -> None:
        self.position_label.configure(
            text=f'Fila: {event.widget.index("insert").split(".")[0]}, Columna: {event.widget.index("insert").split(".")[1]}')

    def manejoOpciones(self, opcion):
        if(opcion == 1):
            Nuevo(self.txtArea)
        if(opcion == 2):
            Abrir(self.txtArea)
        if(opcion == 3):
            Guardar(self.txtArea)
        if(opcion == 4):
            GuardarComo(self.txtArea)  
        if(opcion == 5):
            print("Opcion 5")
        if(opcion == 6):
            print("Opcion 6")
        if(opcion == 7):
            mb.showinfo('Temas de Ayuda',
                                    'Nombre:\n\tBrian Estuardo Ajuchán Tococh\n\nCarné:\n\t202001086\n'
                                    'Curso:\n\t Lab. Lenguajes Formales y de Programación')

    def Analizar(self):
        global tokens_global
        global error_global
        
        analizar = str(self.txtArea.get(1.0, END))
        tkns, error, reconocido = instruccion(analizar)
        if len(error_lexemas)>0:
            mb.showerror("ERROR", "Se encontro uno o mas errores en el archivo de entrada")
            for res in error_lexemas:
                respuesta = (res.getTipo()+": " + str(res.getLexema())+" Fila: "+str(res.getFila())+" Columna: "+str(res.getColumna())+"\n")
                self.txtArea2.insert(END,respuesta)
                tokens_global = tkns
                error_global = error
        else:
            mb.showinfo("Información", "Analisis Completo")
            tokens_global = tkns
            salida = analizador_sintac.analizar(reconocido)
            for res in salida:
                texto = str(res)+"\n"
                self.txtArea2.insert(END, texto)

        
    
        #for ask in error_sin:
        #    print(ask)
    #tokens_global = tkns

def verTokens():
    global tokens_global
    ventana = Tk()
    ventana.title("LISTA DE TOKENS")
    ancho_ventana = 800
    alto_ventana = 600
    x_ventana = ventana.winfo_screenwidth() 
    y_ventana = ventana.winfo_screenheight() 
    pwidth = round(x_ventana/2-ancho_ventana/2)
    pheight = round(y_ventana/2-alto_ventana/2-45)
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(pwidth) + "+" + str(pheight)
    ventana.geometry(posicion)
    ventana.config(borderwidth=20, bg="CadetBlue4")
    lbltokens = Label (ventana, text="Lista de tokens", font=('Comic Sans MS', 20), bg = "CadetBlue4")
    lbltokens.pack()
    btn_Regresar = Button(ventana, text= "Regresar", command=ventana.destroy)
    btn_Regresar.place(x=350, y=505, height= 30, width=100)
    
    columnas = ("num","token","lexema","fila","col")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
    tabla.column("num", stretch=False, width=35)
    tabla.heading('num', text='No.')
    tabla.column("token", stretch=False, width=175)
    tabla.heading('token', text='Token')
    tabla.column("lexema", stretch=False, width=165)
    tabla.heading('lexema', text='Lexema')
    tabla.column("fila", stretch=False, width=125)
    tabla.heading('fila', text='Fila')
    tabla.column("col", stretch=False, width=125)
    tabla.heading('col', text='Columna')
    conta = 1
    for token in tokens_global:
        dato = str(conta),token.getTipo(),token.getLexema(),str(token.getFila()),str(token.getColumna())
        tabla.insert("", END, values=dato)
        conta += 1
    tabla.place(x= 65, y = 75, height=400, width=630)

    ventana.resizable(False, False)

def verErrores():
    global error_global
    ventana = Tk()
    ventana.title("LISTA DE ERRORES")
    ancho_ventana = 800
    alto_ventana = 600
    x_ventana = ventana.winfo_screenwidth() 
    y_ventana = ventana.winfo_screenheight() 
    pwidth = round(x_ventana/2-ancho_ventana/2)
    pheight = round(y_ventana/2-alto_ventana/2-45)
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(pwidth) + "+" + str(pheight)
    ventana.geometry(posicion)
    ventana.config(borderwidth=20, bg="CadetBlue4")
    lbltokens = Label (ventana, text="Lista de Errores", font=('Comic Sans MS', 20), bg = "CadetBlue4")
    lbltokens.pack()
    btn_Regresar = Button(ventana, text= "Regresar", command=ventana.destroy)
    btn_Regresar.place(x=350, y=505, height= 30, width=100)
    
    columnas = ("num","token","lexema","fila","col")
    tabla = ttk.Treeview(ventana, columns=columnas, show="headings")
    tabla.column("num", stretch=False, width=125)
    tabla.heading('num', text='No.')
    tabla.column("token", stretch=False, width=125)
    tabla.heading('token', text='Token')
    tabla.column("lexema", stretch=False, width=125)
    tabla.heading('lexema', text='Lexema')
    tabla.column("fila", stretch=False, width=125)
    tabla.heading('fila', text='Fila')
    tabla.column("col", stretch=False, width=125)
    tabla.heading('col', text='Columna')
    conta = 1
    for token in error_global:
        dato = str(conta),token.getTipo(),token.getLexema(),str(token.getFila()),str(token.getColumna())
        tabla.insert("", END, values=dato)
        conta += 1
    tabla.place(x= 65, y = 75, height=400, width=630)

    ventana.resizable(False, False)

def main(): 
   app = Inicio()

if __name__ == "__main__":
    main()