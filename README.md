# AdivinaElN-mero


Mi dirección de Githup para este repositorio es el siguiente:[Githup](https://github.com/albabernal03/AdivinaElN-mero.git)
https://github.com/albabernal03/AdivinaElN-mero.git

Hemos resuelto un juego de adivinar un número, que se encuentra en un determinado rango dependiendo del nivel seleccionado. En total hay cuatro niveles:
1. Nivel (0-100) 
2. nivel (0-1000)
3. Nivel (0-1000000)
4. Nivel (0-1000000000000)

El diagrama de flujo es el siguiente:

![DIAGRAMA DE FLUJO](https://user-images.githubusercontent.com/91721875/141657773-eefa258c-38dd-4c2a-9db6-aad4826eb70d.jpg)

```
import random 

def jugar(nivel):
    intentos = 0 
    rangoMax = 0
    mensaje = ''
    aleatorio = 0
    intentosMax = 0
    puntuacion = 1000

    if nivel == 1:
        aleatorio = random.randrange(0,100)
        rangoMax= 100
        intentosMax = 10
    elif nivel == 2:
        aleatorio == random.randrange(0,1000)
        rangoMax = 1000
        intentosMax = 20
    elif nivel == 3:
        aleatorio = random.randrange(0,1000000)
        rangoMax = 1000000
        intentosMax = 100
    elif nivel == 4:
        aleatorio = random.randrange(0,1000000000000)
        rangoMax = 1000000000000
        intentosMax = 500
    else:
        aleatrorio = random.randrange(0,100)
        rangoMax= 100
        intentosMax = 10
    
    mensaje = 'Adivina el número (0-' + str(rangoMax) + '): '
    numero = int(input(mensaje))

    while numero != aleatorio and intentos <= intentosMax:
        if numero >aleatorio:
            print('Se ha pasado!')
        else:
            print('Se ha quedado corto!')

        if nivel == 1:
            puntuacion -= 1
        elif nivel == 2:
            puntuacion -= 5
        elif nivel  == 3:
            puntuacion -= 10
        elif nivel == 4:
            puntuacion -= 15
        else:
            puntuacion -= 1
        
        
        numero = int(input(mensaje))
        intentos += 1
    
    if numero != aleatorio:
        print('Has perdido!')
        print('Número máximo de intentos superado!')
    else:
        print('Has adivinado el número', numero)
        print('Cantidad de intentos:', intentos)
        print('Puntuacion final:', puntuacion)

        nombre = input('Indique su nombre: ')
        print('------------------------------------')
        print('NOMBRE      INTENTOS     PUNTUACIÓN')
        print('-------------------------------------')
        print(nombre, '\t' ,intentos, '\t', puntuacion)
        print('--------------------------------------')



def menu():

    print('.::ADIVINA EN NÚMERO::.')
    print('Niveles:')
    print('1. Del 0 al 100')
    print('2. Del 0 al 1.000 ')
    print('3. Del 0 al 1.000.000')
    print('4. Del 0 1.000.000.000.000')
    nivel = int(input('Seleccione un nivel (1-4):'))
    return nivel

def juego():
    nivel = menu()
    print('.::NIVEL SELECCIONADO', nivel, '.:: ')
    jugar (nivel)

juego()
```
