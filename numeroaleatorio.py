
import random

def jugar(nivel):
    


# aleatorio = random.randrange(0,99)
# intentos = 1
# numero = int(input('Adivina el número entre 0 y 99:'))

# while numero != aleatorio:
#     if numero > aleatorio:
#         print ('se ha pasado!')
#     else: 
#         print('se ha quedado corto!')    
    
#     numero = int(input('Adivine el número:'))
#     intentos +=1

# print ( 'Has adivinado el número:', numero)
# print ('Cantidad de intentos:', intentos)

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

