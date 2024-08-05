"""""
Ejercicio 5
Desarrolle un algoritmo que Programa que calcule el precio final de una compra, dado el valor de la
compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la
compra y otra que almacene el valor del descuento. El algoritmo debe mostrar en pantalla, el valor
de la compra el valor del descuento y el valor final a pagar.
"""

print('Tu producto tiene un descuento del 20%')##Imprimo cual es el descuento que tiene el producto
compra = int(input('Ingresa el coste de tu compra: '))##declaro una variable compra en entero, para que el usuario coloque el valor
descuento = compra * 0.2 ##Declaro la variable descuento, y le agrego la operacion del descuento
descuento = int (descuento)  ##Hago un casteo de la variable descuento para que sea exacto
print(f'La compra fue {compra}, con un descuento de {descuento}')##Imprimo el coste de la compra y el descuento que tiene
compra -= descuento ##Le resto a compra el descuento
print(f'El valor final a pagar es: {compra}') ##El valor de la compra actualizado con la resta
