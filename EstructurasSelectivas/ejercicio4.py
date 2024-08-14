"""
En un supermercado se hace una promoción, mediante el cual el cliente obtiene un descuento dependiendo de un color que 
se escoge al azar (...)
"""

import random

colors = [
    'rojo',
    'verde',
    'azul', ##Quise hacer un array de manera distinta instru, por eso esta de esa forma :)
    'amarillo',
    'negro'
]

producto = int(input('Ingresa el valor de tu prodcuto: '))
balota = random.choice(colors)


print(f'El color sacado es {balota}')

if balota == 'rojo':
    descuento = producto * 0.15
    valorFinal = producto - descuento
    print(f'El valor de la comrpra {producto}, el color de la balota {balota}, y valor final es {valorFinal}')
elif balota == 'verde':
    descuento = int(producto * 0.2)
    valorFinal = producto - descuento
    print(f'El valor de la compra {producto}, el color de la balota {balota}, y el valor final es {valorFinal}')
else:
    print(f'El otro color escogido es: {balota}')

