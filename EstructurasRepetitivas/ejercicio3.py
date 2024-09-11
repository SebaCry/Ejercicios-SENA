"""Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja
de todo el grupo."""

max = 0 ## Se crea una variable con un limite que se igual a 0
min = 100 ## Se crea una variable con un limite que sea de 100
notaProm = 0 ## Se crea un acumulador que sume el promedio por cada estudiante


for i in range(0, 20): ## Se crea un bucle que repita los procedimientos 20 veces (20 estudiantes)
    nota = int(input('Ingresa tu nota: ')) ## Se crea una variable nota que guarde dicha nota digitada
    notaProm += nota ## A la variable notaProm va ir acumulando las notas que se registren

    if nota < min: ## Se hace una validacion si la nota es menor al limite de 20                          #HAY QUE TENER EN CUENTA QUE LA NOTA MIN Y MAX VAN A ESTAR CAMBIANDOSE A MEDIDA QUE EL USUARIO REGISTRE NOTAS#
        min = nota ## La nota minima va hacer, la nota registrada
    
    if nota > max: ## De lo contrario si la nota es mayor al limite de 0
        max = nota ## La nota maxima va hacer, la nota registrada            

promedio = notaProm / 20 ## Se saca el promedio, con el acumulador dividiendolo por la cantidad de estudiantes

print(f'La calificacion mas alta del promedio es {max} y la nota mas minima del promedio es {min}. El promedio total es {promedio}') ## Se imprime cual fue la nota maxima, minima, y el promedio de los estudiantes 