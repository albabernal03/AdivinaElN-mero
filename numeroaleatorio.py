import random
aleatorio = random.randrange(0,99)
intentos = 1
numero = int(input('Adivina el número entre 0 y 99:'))

while numero != aleatorio:
    if numero > aleatorio:
        print ('se ha pasado!')
    else: 
        print('se ha quedado corto!')    
    
    numero = int(input('Adivine el número:'))
    intentos +=1

print ( 'Has adivinado el número:', numero)
print ('Cantidad de intentos:', intentos)
