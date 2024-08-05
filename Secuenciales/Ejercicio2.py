"""""
Ejercicio 2
Construya un algoritmo que calcule el perímetro y el área de un rectángulo dada su base y su altura.
La base y la altura deberán ser almacenadas previamente en dos variables respectivamente. El
algoritmo debe mostrar en pantalla el siguiente mensaje: El perímetro del rectángulo es: xxx el área del rectángulo es: yyyy
"""

base = int(input('Ingresa el valor de la base: '))##En la linea 1 declaro la variable base para que el usuario coloque el numero
altura = int(input('Ingresa el valor de la altura: '))##En la linea 2 declaro la variable altura para que el usuario coloque el numero
p = 2*(base + altura)##En la linea 3 hago la operación del perimetro, multiplicando 2 * base + altura, ya que hay 2 bases iguales y 2 alturas iguales
a = base * altura##En la linea 4 hago la operacion del area , multiplicando base * altura
print(f'El perimetro del rectangulo es: {p}, y el area del rectangulo es: {a} ')##En la linea 5 imprimo el valor del perimetro y el area usando concatenacion f'String'
