import turtle
import random

#ventana
wn = turtle.Screen()
wn.title('happy x-mas')
wn.bgcolor('green')
wn.setup(width = 800, height = 600)
wn.tracer(0)


#texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("red")
texto.penup()
texto.hideturtle()
texto.goto(0, 100)
texto.write("Happy", font = 200)
texto.goto(0, -100)
texto.write("christmas", font = 200)

while True:
    wn.update()