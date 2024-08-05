"""""
Ejercicio 1
##Desarrolle un programa que declare tres variables. La primera guardará el nombre del estudiante
##la segunda el nombre del colegio, la tercera el grado que cursa. Y luego imprima el siguiente
##mensaje: “El estudiante xxxx estudia en el yyyy el programa de formación zzzz”
"""

nombre = str(input('Ingresa tu nombre')); nombreInstitucion = str(input('Ingresa el nombre de tu colegio')) ; ##En la linea 1 declaro las variables nombre y nombreInstitucion
nombreFormacion = str(input('Ingresa el nombre de tu colegio'))## En la linea 2 declaro la variable nombreFormacion

print(f'El aprendiz {nombre} estudia en el {nombreInstitucion} y el programa de formación es {nombreFormacion}')##En la linea 4 escribo en mi consola, el resultado que puso el usuario en las variables concatenando f'String'

