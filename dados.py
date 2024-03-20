from random import randint

#dados
dado1 = 0
dado2 = 0

#funciones
def tirardado1():
    return randint(1, 6)

def tirardado2():
    return randint(1, 6)

def jugar():
    dado1 = tirardado1()
    dado2 = tirardado2()
    print('El primer dado cayo en: ', dado1)
    print('El segundo dado cayo en: ', dado2)
    print('La suma de sus valores es: ', dado1 + dado2)

#presentacion
name = input('Cual es tu nombre? ')
print('Hola ', name, '!')
print('Juguemos a los dados!!!')
print('Acabo de tirar los dados! aqui van sus valores.')
jugar()
print('Quieres volver a jugar?')
print('Si quieres volver a jugar presiona 1, por lo contrario presiona 2.')
respuesta = int(input())


while respuesta == 1:
    print('Genial! Aqui vamos de nuevo.')
    jugar()
    print('Excelente partida',name,'!')
    print('Quieres volver a jugar?')
    print('Si quieres volver a jugar presiona 1, por lo contrario presiona 2')
    respuesta = int(input())


print('Ok! hasta luego ', name)






