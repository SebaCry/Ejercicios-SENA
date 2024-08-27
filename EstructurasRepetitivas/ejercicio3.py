max = 0
min = 20
notaProm = 0


for i in range(1, 20):
    nota = int(input('Ingresa tu nota: '))
    notaProm += nota
    if nota < min:
        min = nota
    elif nota > max:
        max = nota
promedio = notaProm / 20

print(f'La calificacion mas alta del promedio es {max} y la nota mas minima del promedio es {min}. El promdio total es {promedio}')

