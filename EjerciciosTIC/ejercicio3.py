'''
Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es par o impar.
'''

for i in range(1,10):
    numero = int(input('Ingresa un numero: '))
    if numero % 2 == 0:
        print('El numero es par')
    else:
        print('El numero es impar')