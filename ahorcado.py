import random
IMAGENESAHORCADO = ['''

   +---+
   |   |
       |
       |
       |
       |
  =======''', '''
  
   +---+
   |   |
   O   |
       |
       |
       |  
  ========''', '''
  
   +---+
   |   |
   O   |
   |   |
       |
       |
  ========''', '''
  
   +---+
   |   |
   O   |
  /|   |
       |
       |
  =========''', '''
  
   +---+
   |   |
   O   |
  /|\  |
       |   
       |
  =========''', '''
  
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
  =========''', '''
  
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 ==========''']
palabras = 'hormiga babuino murcielago oso castor camello gato almeja cobra pantera coyote ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente vaca langostino cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.slipt()

def obtenerPalabraAlAzar(listadepalabras):
    #esta funcion devuelve una cadena al azar de la lista de cadenas pasada como argumento
    indicedepalabras = random.randint(0, len(palabras) - 1)
    return palabras[indicedepalabras]

def mostrartablero(IMAGENESAHORCADO, letrasincorrectas, letrascorrectas, palabrasecreta):
    print(IMAGENESAHORCADO[len(letrasincorrectas)])
    print()

    print('letras incorrectas: ', end=' ')
    for letras in letrasincorrectas
        print(letras, end=' ')
    print()

    espaciosvacios = '_' * len(palabrasecreta)

    for i in range(len(palabrasecreta)): #completar espacios vacios con la letras adivinadas
        if palabrasecreta[i] in letrascorrectas:
            espaciosvacios = espacios vacios[:i] + palabrasecreta[i] + espaciosvacios[i + 1:]

    for letras in espaciosvacios: #mostrar la palabra secreta con espacios entre cada letra
        print(letras, end=' ')
    print()

def obtenerintento(letrasprobadas):
    #devuelve la letra ingresada por el jugador. Verifica  que eljugador ha ingresado una sola letra y no otra cosa.
    while True:
        print('Adivina una letra')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('por favor introduce una letra')
        elif intento in letrasprobadas:
            print('Ya has probado esa letra')
        elif intento not in 'abcdefghijklmnopqrstuwxyz':
            print('por favor ingresa una letra.')
        else:
            return intento

def jugardenuevo():
    #Esta funcion devuelve true al jugador si quiere jugar de nuevo, en contrario devuelve false
    print('Quieres jugar de nuevo?(si o no)') 
    return input().lower().startswith('s')


print('A H O R C A D O')
letrasincorrectas = ''
letrascorrectas = ''
palabrasecreta = obtenerPalabraAlAzar(words) 
juegoterminado = False

while True:
    mostrartablero(IMAGENESAHORCADO, letrasincorrectas, letrascorrectas, palabrasecreta)

    #permite al jugsf=dor escribir una letra
    intento = obtenerintento(letrasincorrectas + letrascorrectas)

    if intento in palabrasecreta:
        letrascorrectas = letrascorrectas + intento

        #verifica si el jugador ha ganado 
        encontradotodaslasletras = True
        for i in range(len(palabrasecreta)):
            if palabrasecreta[i] not in letrascorrectas:
                encontradotodaslasletras = False
                break 
        if encontradotodaslasletras:
            print('Si, la palabra secreta es ' + palabrasecreta + '!  Has ganado!!')
            juegoterminado = True
        else:
            letrasincorrectas = letrasincorrectas + intento

            #comprobar si el jugador  ha agotado sus intentod y ha perdido
            if len(letrasincorrectas) == len(IMAGENESAHORCADO) - 1:
                mostrartablero(IMAGENESAHORCADO, letrasincorrectas, letrascorrectas, palabrasecreta) 
                print('Te has quedado sin intentos!\nDespues de ' + str(len(letrasincorrectas)) + 'intentos fallidos y ' + str(len(letrascorrectas)) + 'aciertos, la palabra era ' + palabrasecreta) 
                juegoterminado = True 

            #preguntar al jugador si quiere voolver a jugar
            if juegoterminado:
                if jugardenuevo():
                    letrasincorrectas = ''
                    letrascorrectas = ''
                    juegoterminado = False 
                    palabrasecreta = obtenerPalabraAlAzar(palabras)
                else:
                    break                

