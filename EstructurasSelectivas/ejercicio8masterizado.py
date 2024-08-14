"""Tomando como base los resultados obtenidos en un laboratorio de analsis clinicos, un medico determina si una persona tiene anemia o no, lo cual
depende de su nivel de hemoglobina en la sangre, de su edad y sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde
, se determina su resultado como positivo, y en caso contrario como negativo"""
print('¿Tienes Anemia?\n')
print('Femeninio || Masculino')

edadTipo = str(input('¿Eres un bebe, niño o adulto?: ')).lower().strip()
hemoglobina = float(input('¿Cual es tu rango de hemoglobina actual?🤨: '))

if edadTipo == 'bebe':
    edadMeses = int(input('¿Cuantos meses tienes?: '))
    if edadMeses == 0 or edadMeses == 1:
        print('Rango Hemeblogina: 13 - 26g')
        if hemoglobina < 13 or hemoglobina > 26:
            print('Positivo para anemia, lo sentimos 😥')
        else:
            print('Negativo para hemoglobina 😉')
    elif edadMeses > 1 and edadMeses <= 6:
        print('Rango Hemeblogina: 10 - 18g')
        if hemoglobina < 10 or hemoglobina > 18:
            print('Positivo para anemia, lo sentimos 😥')
        else:
            print('Negativo para hemoglobina 😉')
    elif edadMeses > 6 and edadMeses <= 12:
        print('Rango Hemeblogina: 11 - 15g')
        if hemoglobina < 8 or hemoglobina > 16:
            print('Positivo para anemia, lo sentimos 😥')
        else:
            print('Negativo para hemoglobina 😉')
elif edadTipo == 'niño':
    edadNiño = int(input('¿Cuantos años tienes?: '))
    if edadNiño <= 15 and edadNiño > 1: 
        if edadNiño > 10:
            print('Rango Hemeblogina: 13 - 15.5g')
            if hemoglobina < 13 or hemoglobina > 15.5:
                print('Positivo para anemia, lo sentimos 😥')
            else:
                print('Negativo para hemoglobina 😉')
    
    elif edadNiño > 5 and edadNiño <= 10:
        print('Rango Hemeblogina: 12.6 - 15.5g')
        if hemoglobina < 12.6 or hemoglobina > 15.5:
            print('Positivo para anemia, lo sentimos 😥')
        else:
            print('Negativo para hemoglobina 😉')
    
    elif edadNiño > 1 and edadNiño <= 5:
        print('Rango Hemeglobina: 11.5 - 15')
        if hemoglobina < 11.5 or hemoglobina >15:
            print('Positivo para anemia, lo sentimos 😥')
        else:
            print('Negativo para hemoglobina 😉')
    else:
        print('Escribe un digito coherente')
elif edadTipo == 'adulto':
    edadAdulto = int(input('¿Cuantos años tienes?: '))
    sex = str(input('¿Cual es tu sexo?: ')).lower().strip()
    if sex == 'femenino' and edadAdulto > 15:
        print('Rango Hemeblogina: 12 - 16g')
        if hemoglobina < 12 or hemoglobina > 16:
            print('Positivo para anemia, lo sentimos 😥')
        else:
            print('Negativo para hemoglobina 😉')
    elif sex == 'masculino' and edadAdulto > 15:
        print('Rango Hemeblogina: 14 - 18g')
        if hemoglobina < 14 or hemoglobina > 18:
            print('Positivo para anemia, lo sentimos 😥')
        else:
            print('Negativo para hemoglobina 😉')
    else:
        print('Escribe un digito coherente')