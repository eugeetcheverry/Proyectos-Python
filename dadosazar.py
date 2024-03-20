from random import randint

#dados
dado1 = 0
dado2 = 0

#funciones
def tirada1():
    return randint(1, 6)

def tirada2():
    return randint(1, 6)

def tirardados():
    dado1 = tirada1()
    dado2 = tirada2()
    print('El primer dado cayo en: ', dado1)
    print('El segundo dado cayo en: ', dado2)
    print('El valor de su suma es: ', dado1 + dado2)


#interaccion con el usuario

tirar =('')
name = input('Cual es tu nombre?')
print('Hola ', name, '!')
print('Quieres tirar los dados?')
tirar = input("")

while tirar == 'S' or 's':
    tirardados()
    print('Quieres tirar los dados?')
    tirar = input("")



