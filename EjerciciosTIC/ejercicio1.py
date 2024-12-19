'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla
si es mayor de edad o no.
'''

while True:
    try:
        edad = int(input('Ingresa tu edad: '))
        

        if edad >= 18:
            print('Usted se considera mayor de edad')
        elif edad < 18 and edad > 0:
            print('Usted se considera menor de edad')
        else:
            print('Ingresa una edad en años.')
            continue

        salir = str(input('¿Quieres salir del bucle? Si o No: ')).lower()

        if salir == 'si':
            break
        else:
            continue
    except ValueError as error:
        print(f'Ingresa un valor correcto. Acá esta tu error: {error}')