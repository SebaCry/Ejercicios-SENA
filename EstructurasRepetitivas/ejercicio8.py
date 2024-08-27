estudiantes1 = 0
estudiantes2 = 0
estudiantes3 = 0
estudiantes4 = 0

for estudiante in range(0,23):
    nota = int(input('¿Cual fue tu calificacion de 1 - 100?: '))
    if nota < 50:
        estudiantes1 += 1
    elif nota >= 50 and nota < 70:
        estudiantes2 += 1
    elif nota >= 70 and nota < 80:
        estudiantes3 += 1
    elif nota >= 80:
        estudiantes4 += 1

print(f'Esudiantes menores a 50: {estudiantes1}\n Estudiantes mayores de 50 pero menores de 70: {estudiantes2}\n Estudiantes mayores de 70 pero menores de 80: {estudiantes3}\n Estudiantes mayores a 80: {estudiantes4}')
