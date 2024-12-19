"""""
Ejercicio 3
Elabore un algoritmo que calcule el promedio de tres números, los cuales deben ser almacenados
previamente en tres variables. El algoritmo debe imprimir el siguiente mensaje: El promedio de los números ingresado es: xxxx
"""

num1 = float(input('Ingresa tu nota 1: '))##En la linea 1 declaro la variable num1 como float para que la nota tenga decimal, y el usuario coloque
num2 = float(input('Ingresa tu nota 2: '))##En la linea 2 declaro la variable num2 como float para que la nota tenga decimal, y el usuario coloque
num3 = float(input('Ingresa tu nota 3: '))##En la linea 3 declaro la variable num3 como float para que la nota tenga decimal, y el usuario coloque
prom = (num1 + num2 + num3) / 3 ## En la linea 4 Hago una variable prom que realice la operacion del promedio de las notas, sumandolas y dividiendolas por la cantidad de notas que hay
print(f'El promedio de los numeros ingresados es: {prom}')##En la linea 5 imprimo en la consola cual fue el promedio de los numeros ingresados
