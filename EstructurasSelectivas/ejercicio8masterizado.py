"""Tomando como base los resultados obtenidos en un laboratorio de analsis clinicos, un medico determina si una persona tiene anemia o no, lo cual
depende de su nivel de hemoglobina en la sangre, de su edad y sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde
, se determina su resultado como positivo, y en caso contrario como negativo"""
##Instru cabe aclarar que esta es una forma extensa usando las estructuras selectivas anidadas. Se puede resumir mas el code, pero lo hice usando las estructuras selectivas anidadas 
print('¿Tienes Anemia?\n') ## Imprimo el nombre del programa para indicar la pregunta principal.
print('Femeninio || Masculino') ## Pregunto al usuario si es femenino o masculino para ajustar los parámetros de hemoglobina.

edadTipo = str(input('¿Eres un bebe, niño o adulto?: ')).lower().strip() ## Solicito al usuario su tipo de edad (bebé, niño o adulto) y estandarizo la entrada a minúsculas y sin espacios extra.
hemoglobina = float(input('¿Cual es tu rango de hemoglobina actual?🤨: ')) ## Solicito el nivel de hemoglobina del usuario y lo convierto a un número decimal.

if edadTipo == 'bebe': ## Si el usuario es un bebé
    edadMeses = int(input('¿Cuantos meses tienes?: ')) ## Solicito la edad en meses para bebés y la convierto a un número entero.
    if edadMeses == 0 or edadMeses == 1: ## Si el bebé tiene 0 o 1 mes
        print('Rango Hemoglobina: 13 - 26g') ## Indico el rango de hemoglobina adecuado para la edad.
        if hemoglobina < 13 or hemoglobina > 26: ## Verifico si el nivel de hemoglobina está fuera del rango adecuado
            print('Positivo para anemia, lo sentimos 😥') ## Informo que el usuario tiene anemia si el nivel está fuera del rango.
        else:
            print('Negativo para hemoglobina 😉') ## Informo que el usuario no tiene anemia si el nivel está dentro del rango.
    elif edadMeses > 1 and edadMeses <= 6: ## Si el bebé tiene entre 2 y 6 meses
        print('Rango Hemoglobina: 10 - 18g') ## Indico el rango de hemoglobina adecuado para esta edad.
        if hemoglobina < 10 or hemoglobina > 18: ## Verifico si el nivel de hemoglobina está fuera del rango adecuado.
            print('Positivo para anemia, lo sentimos 😥') ## Informo que el usuario tiene anemia si el nivel está fuera del rango.
        else:
            print('Negativo para hemoglobina 😉') ## Informo que el usuario no tiene anemia si el nivel está dentro del rango.
    elif edadMeses > 6 and edadMeses <= 12: ## Si el bebé tiene entre 7 y 12 meses
        print('Rango Hemoglobina: 11 - 15g') ## Indico el rango de hemoglobina adecuado para esta edad.
        if hemoglobina < 8 or hemoglobina > 16: ## Verifico si el nivel de hemoglobina está fuera del rango adecuado.
            print('Positivo para anemia, lo sentimos 😥') ## Informo que el usuario tiene anemia si el nivel está fuera del rango.
        else:
            print('Negativo para hemoglobina 😉') ## Informo que el usuario no tiene anemia si el nivel está dentro del rango.

elif edadTipo == 'niño': ## Si el usuario es un niño
    edadNiño = int(input('¿Cuantos años tienes?: ')) ## Solicito la edad en años y la convierto a un número entero.
    if edadNiño <= 15 and edadNiño > 1: ## Si el niño tiene entre 2 y 15 años
        if edadNiño > 10: ## Si el niño tiene más de 10 años
            print('Rango Hemoglobina: 13 - 15.5g') ## Indico el rango de hemoglobina adecuado para esta edad.
            if hemoglobina < 13 or hemoglobina > 15.5: ## Verifico si el nivel de hemoglobina está fuera del rango adecuado.
                print('Positivo para anemia, lo sentimos 😥') ## Informo que el usuario tiene anemia si el nivel está fuera del rango.
            else:
                print('Negativo para hemoglobina 😉') ## Informo que el usuario no tiene anemia si el nivel está dentro del rango.
    
    elif edadNiño > 5 and edadNiño <= 10: ## Si el niño tiene entre 6 y 10 años
        print('Rango Hemoglobina: 12.6 - 15.5g') ## Indico el rango de hemoglobina adecuado para esta edad.
        if hemoglobina < 12.6 or hemoglobina > 15.5: ## Verifico si el nivel de hemoglobina está fuera del rango adecuado.
            print('Positivo para anemia, lo sentimos 😥') ## Informo que el usuario tiene anemia si el nivel está fuera del rango.
        else:
            print('Negativo para hemoglobina 😉') ## Informo que el usuario no tiene anemia si el nivel está dentro del rango.
    
    elif edadNiño > 1 and edadNiño <= 5: ## Si el niño tiene entre 2 y 5 años
        print('Rango Hemoglobina: 11.5 - 15g') ## Indico el rango de hemoglobina adecuado para esta edad.
        if hemoglobina < 11.5 or hemoglobina > 15: ## Verifico si el nivel de hemoglobina está fuera del rango adecuado.
            print('Positivo para anemia, lo sentimos 😥') ## Informo que el usuario tiene anemia si el nivel está fuera del rango.
        else:
            print('Negativo para hemoglobina 😉') ## Informo que el usuario no tiene anemia si el nivel está dentro del rango.
    else:
        print('Escribe un dígito coherente') ## Mensaje de error si la edad no está dentro de los rangos válidos.

elif edadTipo == 'adulto': ## Si el usuario es un adulto
    edadAdulto = int(input('¿Cuantos años tienes?: ')) ## Solicito la edad en años y la convierto a un número entero.
    sex = str(input('¿Cual es tu sexo?: ')).lower().strip() ## Solicito el sexo del usuario, estandarizo la entrada a minúsculas y quito espacios extra.
    if sex == 'femenino' and edadAdulto > 15: ## Si el usuario es femenino y tiene más de 15 años
        print('Rango Hemoglobina: 12 - 16g') ## Indico el rango de hemoglobina adecuado para mujeres adultas.
        if hemoglobina < 12 or hemoglobina > 16: ## Verifico si el nivel de hemoglobina está fuera del rango adecuado.
            print('Positivo para anemia, lo sentimos 😥') ## Informo que el usuario tiene anemia si el nivel está fuera del rango.
        else:
            print('Negativo para hemoglobina 😉') ## Informo que el usuario no tiene anemia si el nivel está dentro del rango.
    elif sex == 'masculino' and edadAdulto > 15: ## Si el usuario es masculino y tiene más de 15 años
        print('Rango Hemoglobina: 14 - 18g') ## Indico el rango de hemoglobina adecuado para hombres adultos.
        if hemoglobina < 14 or hemoglobina > 18: ## Verifico si el nivel de hemoglobina está fuera del rango adecuado.
            print('Positivo para anemia, lo sentimos 😥') ## Informo que el usuario tiene anemia si el nivel está fuera del rango.
        else:
            print('Negativo para hemoglobina 😉') ## Informo que el usuario no tiene anemia si el nivel está dentro del rango.
    else:
        print('Escribe un dígito coherente') ## Mensaje de error si el tipo de edad o sexo no es válido.