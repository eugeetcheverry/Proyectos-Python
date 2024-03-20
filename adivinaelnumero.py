import random 

intentosrealizados = 0

print('hola!, como te llamas?')
nombre = input()

numero = random.randint(1, 20)
print('bueno ' + nombre + 'estoy pensando en un numero entre el 1 y el 20. Intenta adivinar')

while intentosrealizados < 6:
    print('intenta adivinar')
    estimacion = input()
    estimacion = int(estimacion)

    intentosrealizados = intentosrealizados + 1

    if estimacion < numero:
        print('tu estimacion es muy baja')

        if estimacion > numero:
            print('tu estimacion es muy alta')


    if estimacion == numero:
      break

if estimacion == numero:
    intentosrealizados = str(intentosrealizados)
    print('buen trabajo, '+ nombre + 'has adivinado mi numero en '+ intentosrealizados + 'intentos!')

if estimacion != numero:
    numero = str(numero)
    print("pues no, el numero que estaba pensando era" + numero)

