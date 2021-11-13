import random 

def jugar(nivel):
    intentos = 0 
    rangoMax = 0
    mensaje = ''
    aleatorio = 0

    if nivel == 1:
        aleatorio = random.randrange(0,100)
        rangoMax= 100
    elif nivel == 2:
        aleatorio == random.randrange(0,1000)
        rangoMax = 1000
    elif nivel == 3:
        aleatorio = random.randrange(0,1000000)
        rangoMax = 1000000
    elif nivel == 4:
        aleatorio = random.randrange(0,1000000000)
        rangoMax = 10000000000
    else:
        aleatrorio = random.randrange(0,100)
        rangoMax= 100
    
    mensaje = 'Adivina el número (0-' + str(rangoMax) + '): '
    numero = int(input(mensaje))

    while numero != aleatorio:
        if numero >aleatorio:
            print('Se ha pasado!')
        else:
            print('Se ha quedado corto!')
        
        numero = int(input(mensaje))
        intentos += 1

    print ('Has adivinado el número', numero)
    print ('Cantidad de intentos:', intentos)


def menu():

    print('.::ADIVINA EN NÚMERO::.')
    print('Niveles:')
    print('1. Del 0 al 100')
    print('2. Del 0 al 1000 ')
    print('3. Del 0 al 1000000')
    print('4. Del 0 1000000000')
    nivel = int(input('Seleccione un nivel (1-4):'))
    return nivel

def juego():
    nivel = menu()
    print('.::NIVEL SELECCIONADO', nivel, '.:: ')
    jugar (nivel)

juego()