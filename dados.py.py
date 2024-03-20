import turtle
from random import randint 

#ventana
wn = turtle.Screen()
wn.title('Dados')
wn.bgcolor('grey')
wn.setup(width = 800, height = 600)
wn.tracer(0)


name = turtle.textinput("datos", "name")

#texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("black")
texto.penup() #borra el rastro de la escritura
texto.hideturtle()
texto.goto(0, 230)
texto.write("Hola {}!".format(name), align = "center", font= ("Courier", 30, "normal"))
texto.goto(0, 205)
texto.write("Para tirar el primer dado presiona 'w' y para el segundo 'd'", align = "center", font= ("Courier", 15, "normal"))
texto.goto(0,150)
texto.write("Para obtener su suma presiona la tecla 's'", align = "center", font= ("Courier", 15, "normal"))
texto.goto(0, 100)
texto.write("Si quieres volver a tirar repite las instrucciones!", align = "center", font= ("Courier", 15, "normal"))

#texto dado1
textodado1 = turtle.Turtle()
textodado1.speed(0)
textodado1.color("blue")
textodado1.penup() #borra el rastro de la escritura
textodado1.hideturtle()
textodado1.goto(-200, 0)
textodado1.write("Primer dado: 0", align = "center", font= ("Courier", 24, "normal"))


#Texto dado2
textodado2 = turtle.Turtle()
textodado2.speed(0)
textodado2.color("blue")
textodado2.penup() #borra el rastro de la escritura
textodado2.hideturtle()
textodado2.goto(200, 0)
textodado2.write("Segundo dado: 0", align = "center", font= ("Courier", 24, "normal"))

#texto suma total
sumadados = turtle.Turtle()
sumadados.speed(0)
sumadados.color("red")
sumadados.penup() #borra el rastro de la escritura
sumadados.hideturtle()
sumadados.goto(0, -180)
sumadados.write("El valor de su suma es: 0 ", align = "center", font= ("Courier", 27, "normal"))

#dados
dado1 = 0
dado2 = 0

#sumadados
suma = 0

#funcion dados
def tirada1():
    return randint(1, 6)

def tirada2():
    return randint(1, 6)     
  
def tecla1():
    global dado1
    if tirada1() < 7:
        dado1 = tirada1()
    textodado1.clear()
    textodado1.write("Primer dado: {}".format(dado1), align = "center", font= ("Courier", 24, "normal"))

def tecla2():
    global dado2
    if tirada2() < 7:
        dado2 = tirada2()
    textodado2.clear()
    textodado2.write("Segundo dado: {}".format(dado2), align = "center", font= ("Courier", 24, "normal"))   


def tecla3():
    suma = dado1 + dado2
    sumadados.clear()
    sumadados.write("El valor de su suma es:{}".format(suma), align = "center", font= ("Courier", 24, "normal"))


#teclado
wn.listen()
wn.onkeypress(tecla1, "w")
wn.onkeypress(tecla2, "d")
wn.onkeypress(tecla3, "s")



while True:
    wn.update()

    
    
