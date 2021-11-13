
import random

def jugar(nivel):
    aleatorio = 0
    intentos = 1
    rangoMax = 0
    mensaje = ''

    if nivel == 1:
        aleatorio = random.randrange(0,100)
        rangoMax = 100
    elif nivel == 2:
        aleatorio == random.randrange(0,1000)
        rangoMax = 1000
    elif nivel == 3:
        aleatorio = random.randrange(0,1000000)
        rangoMax = 1000000
    elif nivel == 4:
        aleatorio = random.randrange(0,1000000000000)
        rangoMax = 1000000000000
    else:
        aleatorio = random.randrange(0,100)


mensaje = int(input('Adivina el número entre 0-', rangoMax , ') : )')
numero = int(input(mensaje))


while numero != aleatorio:
     if numero > aleatorio:
        print ('se ha pasado!')
     else: 
         print('se ha quedado corto!')    
    

     numero = int(input('Adivine el número entre 0-', rangoMax , '): '))
    intentos +=1

 print ( 'Has adivinado el número:', numero)
 print ('Cantidad de intentos:', intentos)

def menu():
    print('.::ADIVINA EL NÚMERO:::')
    print('Niveles:')
    print('1. Del 0 al 100')
    print('2. Del 0 al 1000')
    print('3. Del 0 al 1.000.000')
    print('4. Del 0 al 1.000.000.000.000')
    nivel=int(input('Selecciona un nivel(1-4):'))
    return nivel

def juego():
    nivel = menu()
    print('.:NIVEL SELECCIONADO:', nivel,'.::.')
    jugar (nivel)

juego()

