"""
En un supermercado se hace una promoción, mediante el cual el cliente obtiene un descuento dependiendo de un color que 
se escoge al azar (...)
"""

import random ## Importo la libreria random

colors = [
    'rojo',
    'verde',
    'azul', ##Quise hacer un array de manera distinta instru, por eso esta de esa forma, como tipo diccionario :)
    'amarillo',
    'negro'
]

producto = int(input('Ingresa el valor de tu prodcuto: ')) ##Defino el valor de la compra para que usuario digite 
balota = random.choice(colors) ## Elijo un color al azar usando el metodo choice


print(f'El color sacado es {balota}') ##Imprimo el color sacado de la boleta

if balota == 'rojo': ## Si el valor de la boleta es rojo
    descuento = producto * 0.15 ##Al prodcuto se le aplica un descuento del 15%
    valorFinal = producto - descuento ## Se le resta el descuento
    print(f'El valor de la comrpra {producto}, el color de la balota {balota}, y valor final es {valorFinal}') ##   Imprimo el valor de la compra
elif balota == 'verde': ## Si el valor de la boleta es verde
    descuento = int (producto * 0.2) ##Al prodcuto se le aplica un descuento del 20%
    valorFinal = producto - descuento ## Se le resta el descuento
    print(f'El valor de la compra {producto}, el color de la balota {balota}, y el valor final es {valorFinal}') ##   Imprimo el valor de la compra
else:
    print(f'El otro color escogido es: {balota}. Por lo tanto, el valor a pagar es {producto}') ## Ahora si los valores no son verde ni rojo, se le cobra el porcuto normal

