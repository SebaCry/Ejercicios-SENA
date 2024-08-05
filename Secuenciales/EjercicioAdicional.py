nombreEstudiante = str(input('Ingrese su nombre: '))
calificacionEnclase = float(input('Ingrese su calificacion promedio de las actividades realizadas en clase: '))
proyectoFinal = float(input('Ingrese su calificacion del proyecto final: '))
promedioEvaluaciones = float(input('Ingrese el promedio de sus evaluaciones parciales: '))

p1 = calificacionEnclase * 0.3
p2 = proyectoFinal * 0.5
p3 = promedioEvaluaciones * 0.2

suma = p1 + p2 + p3
print(suma)