nombreEstudiante = str(input('Ingrese su nombre: '))##Declaro variable nombreEstudiante como texto y que el usuario coloque
calificacionEnclase = float(input('Ingrese su calificacion promedio de las actividades realizadas en clase: '))##Declaro variable calificacionEnClase como float, para que sea decimal la nota
proyectoFinal = float(input('Ingrese su calificacion del proyecto final: '))##Declaro variable proyectoFinal como float, para que sea decimal la nota
promedioEvaluaciones = float(input('Ingrese el promedio de sus evaluaciones parciales: '))##Declaro variable promedioEvaluaciones como float, para que sea decimal la nota

p1 = calificacionEnclase * 0.3 ##Declaro una variable p1 para hallar la nota segun el porcentaje
p2 = proyectoFinal * 0.5 ##Declaro una variable p2 para hallar la nota segun el porcentaje
p3 = promedioEvaluaciones * 0.2##Declaro una variable p3 para hallar la nota segun el porcentaje

notaFinal = p1 + p2 + p3 ##Sumo las notas segun los porcentajes
print(f'La nota final de algoritmia de {nombreEstudiante} es: {suma}')##Imprimo el nombre del estudiante y la nota final del joven