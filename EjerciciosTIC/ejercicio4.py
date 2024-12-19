'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y 
tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
y muestre por pantalla si el usuario tiene que tributar o no.
'''

while True:
    edad = int(input('Ingresa tu edad: '))
    ingresos = int(input('Ingresa tus ingresos: '))

    if edad > 16 and ingresos >= 1000:
        print('Debes tributar')
    else:
        print('No debe tributar')

    salir = str(input('¿Quieres salir del bucle? Si o No: ')).lower()

    if salir == 'si':
        break
    else:
        continue
