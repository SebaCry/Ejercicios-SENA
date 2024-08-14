print('¿Tienes Anemia?\n')  # Imprimo el nombre del programa

# Pregunto al usuario si es masculino o femenino
sexo = str(input('¿Cual es tu sexo?: ')).lower().strip()

# Pregunto al usuario su edad y género
edad = int(input('¿Cuantos años tienes?: '))

# Defino el rango de hemoglobina que corresponde a cada edad y sexo
if sexo == 'femenino':
    if edad <= 15:
        rango_hemoglobina = (12, 16)
    else:
        rango_hemoglobina = (11.5, 15)
elif sexo == 'masculino':
    if edad <= 15:                                ##ESTRUCTURA CONDICIONAL PARA MAÑANA, ACUERDATE HACERLO ASI, PERO CON E S A
        rango_hemoglobina = (14, 18)
    else:
        rango_hemoglobina = (13, 15.5)
else:
    print('Escribe un digito coherente')
    exit()

# Comparo el nivel de hemoglobina ingresado con el rango correspondiente
if rango_hemoglobina[0] <= hemoglobina <= rango_hemoglobina[1]:
    print('Negativo para hemoglobina 😉')
else:
    print('Positivo para anemia, lo sentimos 😥')