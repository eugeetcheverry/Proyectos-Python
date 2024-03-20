import tkinter

#ventana
ventana = tkinter.Tk() #Creamos la pantalla
ventana.geometry("400x300") # medidad de la ventana

# Boton1 = tkinter.Button(ventana, text = "click")
# Boton2 = tkinter.Button(ventana, text = "click")
# Boton3 = tkinter.Button(ventana, text = "click")

# #posicionar facilmente los botones

# Boton1.grid(row = 0, column = 0)
# Boton2.grid(row = 1, column = 1)
# Boton3.grid(row = 2, column = 2)

# cajatexto = tkinter.Entry(ventana, font = "Helvetica 50") # introducir texto
# cajatexto.pack()

# etiqueta = tkinter.Label(ventana)
# etiqueta.pack()

# def textocaja():
#     text20 = cajatexto.get()
#     etiqueta["text"] = text20 #texto en pantalla introducido por el usuario

# Boton1 = tkinter.Button(ventana, text = "click", command = textocaja)
# Boton1.pack()

# etiqueta = tkinter.Label(ventana, text = "Hola mundo", bg = "blue") #ponemos texto en pantalla
# etiqueta.pack(fill = tkinter.X, expand = True, side = tkinter.RIGHT) #imprimimos en panalla

# def saludo(nombre):
#     print("Hola " + nombre)


#boton1 = tkinter.Button(ventana, text = "presiona", padx = 30, pady = 20, command = lambda: saludo("Python"))
#boton1.pack()

ventana.mainloop() #Sirve para mantener la pantalla abierta
