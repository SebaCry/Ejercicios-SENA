print('¿Tienes Anemia?\n')  # Imprimo el nombre del programa

edadTipo = str(input('¿Escoje el tipo de edad (bebe, niño o adulto): ')).lower().strip()
hemoglobina = float(input('¿Cual es tu rango de hemoglobina actual?🤨: '))

if edadTipo == 'bebe':
    edadMeses = int(input('¿Cuantos meses tienes?: '))
    if edadMeses == 0 or edadMeses == 1:
        rangoHemoglobina = (13,26)
    elif edadMeses > 1 and edadMeses <= 6:
        rangoHemoglobina = (10,18)
    elif edadMeses > 6 and edadMeses <= 12:
        rangoHemoglobina = (11,15)
    else:
        print('Escribe un dígito coherente')
elif edadTipo == 'niño':
    edad = int(input('¿Cuantos años tienes?: '))
    if edad >= 1 and edad <= 5:
        rangoHemoglobina = (11.5,15)
    elif edad > 5 and edad <= 10:
        rangoHemoglobina = (12.6,15.5)
    elif edad > 10 and edad <= 15:
        rangoHemoglobina = (13,15.5)
    else:
        print('Escribe un dígito coherente')
elif edadTipo == 'adulto':
    sexo = str(input('¿Cual es tu sexo?: ')).lower().strip()
    if sexo == 'femenino':
        rangoHemoglobina = (12,16)
    elif sexo == 'masculino':
        rangoHemoglobina = (14,18)
    else:
        print('Escribe un dígito coherente')
else:
    print('Escribe un dígito coherente')

if hemoglobina < rangoHemoglobina[0] or hemoglobina > rangoHemoglobina[1]:
    print('Positivo para anemia, lo sentimos 😥')
else:
    print('Negativo para hemoglobina 😉')
