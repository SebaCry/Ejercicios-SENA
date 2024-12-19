'''
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo
impositivo que le corresponde.

10000 y 20000 15
20000 y 35000 20 
35000 y 60000 30
< 60000 40
'''

renta = int(input('Digita tu renta anual: '))

if renta < 10000:
    impositivo = renta * 0.05
    print(f'Tu tipo impositivo según tu renta es de: {impositivo}')
elif 10000 <= renta < 20000:
    impositivo = renta * 0.15
    print(f'Tu tipo impositivo según tu renta es de: {impositivo}')
elif 20000 <= renta < 35000:
    impositivo = renta * 0.20
    print(f'Tu tipo impositivo según tu renta es de: {impositivo}')
elif 35000 <= renta < 60000:
    impositivo = renta * 0.30
    print(f'Tu tipo impositivo según tu renta es de: {impositivo}')
elif renta >= 60000:
    impositivo = renta * 0.40
    print(f'Tu tipo impositivo según tu renta es de: {impositivo}')
else:
    print('Ingresa un valor adecuado')

