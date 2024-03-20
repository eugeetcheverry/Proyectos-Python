import turtle
import time
import msvcrt
import random

posponer = 0.1

#marcador
Score = 0
High_Score = 0

#configuracion de la ventana
wn = turtle.Screen()
wn.title('juego de snake')
wn.bgcolor('black')
wn.setup(width = 600, height = 600)
wn.tracer(0)

#cabexa serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direccion = "stop"

#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#cuerpo serpiente
segmentos = []

#texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0      High Score: 0", align = "center", font = ("Courier", 24, "normal"))


#funciones
def arriba():
    cabeza.direccion = "up"
def abajo():
    cabeza.direccion = "down"
def izquierda():
    cabeza.direccion = "left"
def derecha():
    cabeza.direccion = "right"    


def mov():
    if cabeza.direccion == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direccion == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)    

    if cabeza.direccion == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)    
  
    if cabeza.direccion == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20) 

#teclado
wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")  

while True:
    wn.update()

    #colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor() < -290 or cabeza.ycor() > 290 or cabeza.ycor() < -290:
       time.sleep(1)
       cabeza.goto(0,0)
       cabeza.direccion = "stop"

       #esconder los segmentos
       for segmento in segmentos:
           segmento.goto(1000,1000)

    

        
    #colisiones comida
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("light green")
        nuevo_segmento.penup()
        segmentos.append(nuevo_segmento)

        #aumentar el marcador
        Score += 10

        if Score > High_Score:
            High_Score = Score

        texto.clear()
        texto.write("Score: {}      High Score: {}".format(Score, High_Score), align = "center", font = ("Courier", 24, "normal"))    

    #mover el cuerpo de la serpiente
    totalSeg = len(segmentos) 
    for index in range(totalSeg - 1, 0, -1):
        x = segmentos[index - 1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)  

    mov()
    time.sleep(posponer)
msvcrt.getch()
