## Hola instru, hice otra manera el problema, esta vez simplificando, con el uso de rangos y posiciones
print('¿Tienes Anemia?\n')  # Imprimo el nombre del programa

edadTipo = str(input('¿Escoje el tipo de edad (bebe, niño o adulto): ')).lower().strip() ##Declaro una variable edadTipo, con metodos .lower y .strip, para ponerlas en minusculas y quitar los espacios, tipo string (texto)
hemoglobina = float(input('¿Cual es tu rango de hemoglobina actual?🤨: ')) #Se declara una variable hemoglobina, tipo float, para escribir el rango de hemoglobina

if edadTipo == 'bebe':  # Si el tipo de edad es bebe
    edadMeses = int(input('¿Cuantos meses tienes?: '))  # Se pide la edad del bebé en meses
    if edadMeses == 0 or edadMeses == 1:  # Si el bebé tiene 0 o 1 mes
        rangoHemoglobina = (13,26)  # Se asigna un rango de hemoglobina de 13 a 26
    elif edadMeses > 1 and edadMeses <= 6:  # Si el bebe tiene entre 2 y 6 meses
        rangoHemoglobina = (10,18)  # Se asigna un rango de hemoglobina de 10 a 18
    elif edadMeses > 6 and edadMeses <= 12:  # Si el bebe tiene entre 7 y 12 meses
        rangoHemoglobina = (11,15)  # Se asigna un rango de hemoglobina de 11 a 15
    else:  # Si el usuario ingresa un numero fuera del rango esperado
        print('Escribe un dígito coherente')  # Se muestra un mensaje de error
elif edadTipo == 'niño': ## SI el tipo de edad es niño
    edad = int(input('¿Cuantos años tienes?: ')) #Se pide la edad del niño en años
    if edad >= 1 and edad <= 5:  # Si el niño tiene entre 1 y 5 años
        rangoHemoglobina = (11.5,15)  # Se asigna un rango de hemoglobina de 11.5 a 15
    elif edad > 5 and edad <= 10:  # Si el niño tiene entre 6 y 10 años
        rangoHemoglobina = (12.6,15.5)  # Se asigna un rango de hemoglobina de 12.6 a 15.5
    elif edad > 10 and edad <= 15:  # Si el niño tiene entre 11 y 15 años
        rangoHemoglobina = (13,15.5)  # Se asigna un rango de hemoglobina de 13 a 15.5
    else:  # Si el usuario ingresa un numero fuera del rango esperado
        print('Escribe un dígito coherente')  # Se muestra un mensaje de error
elif edadTipo == 'adulto': # Si el tipo de edad es adulto
    sexo = str(input('¿Cual es tu sexo?: ')).lower().strip() # Se pide que tipo de sexo es
    if sexo == 'femenino':  # Si el sexo es femenino
        rangoHemoglobina = (12,16)  # Se asigna un rango de hemoglobina de 12 a 16
    elif sexo == 'masculino':  # Si el sexo es masculino
        rangoHemoglobina = (14,18)  # Se asigna un rango de hemoglobina de 14 a 18
    else:  # Si el usuario ingresa algo que no es femenino ni masculino
        print('Escribe un dígito coherente')  # Se muestra un mensaje de error
else:
    print('Escribe un tipo de edad CORRECTO :(') ## Si todos los paramentros no se cumplen, sale un mensaje de error

if hemoglobina < rangoHemoglobina[0] or hemoglobina > rangoHemoglobina[1]: ## Si la hemoglobina digitada es menor al primer digito del rango o en mayor al segundo digito del rango segun las edades o meses
    print('Positivo para anemia, lo sentimos 😥') ## Se imprime que posee anemia
else: ## De lo contrario
    print('Negativo para hemoglobina 😉') ## Sale un mensaje alentador jejeje
