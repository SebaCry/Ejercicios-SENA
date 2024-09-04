"""Una persona debe realizar un muestreo con 50 personas para determinar el
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona.
Las categorías se determinar de acuerdo a la siguiente tabla:"""

pesoNiño = 0       # Inicializa la variable para acumular el peso total de los niños
pesoJoven = 0      # Inicializa la variable para acumular el peso total de los jóvenes
pesoAdulto = 0     # Inicializa la variable para acumular el peso total de los adultos
pesoAnciano = 0    # Inicializa la variable para acumular el peso total de los ancianos

niños = 0          # Contador para el número de niños en la muestra
jovenes = 0        # Contador para el número de jóvenes en la muestra
adultos = 0        # Contador para el número de adultos en la muestra
ancianos = 0       # Contador para el número de ancianos en la muestra

for i in range(1, 51):  # Inicia un bucle que se repetirá 50 veces, representando a 50 personas
    edades = int(input('Ingresa tu edad: '))  # Solicita al usuario que ingrese la edad y la almacena en la variable edades
    pesos = int(input('Ingresa tu peso: '))   # Solicita al usuario que ingrese su peso y lo almacena en la variable pesos

    if 0 <= edades <= 12:  # Verifica si la edad está en el rango de 0 a 12 años
        niños += 1         # Incrementa el contador de niños
        pesoNiño += pesos  # Suma el peso ingresado al acumulador de peso de los niños 

    elif 13 <= edades <= 29:  # Verifica si la edad está en el rango de 13 a 29 años
        jovenes += 1           # Incrementa el contador de jóvenes
        pesoJoven += pesos     # Suma el peso ingresado al acumulador de peso de los jóvenes

    elif 30 <= edades <= 59:  # Verifica si la edad está en el rango de 30 a 59 años
        adultos += 1           # Incrementa el contador de adultos
        pesoAdulto += pesos    # Suma el peso ingresado al acumulador de peso de los adultos

    elif edades >= 60:  # Verifica si la edad es 60 años o mayor
        ancianos += 1    # Incrementa el contador de ancianos
        pesoAnciano += pesos  # Suma el peso ingresado al acumulador de peso de los ancianos
        
promedioNiño = pesoNiño / niños  # Calcula el promedio de peso de los niños
promedioJovenes = pesoJoven / jovenes  # Calcula el promedio de peso de los jóvenes
promedioAdultos = pesoAdulto / adultos  # Calcula el promedio de peso de los adultos
promedioAncianos = pesoAnciano / ancianos  # Calcula el promedio de peso de los ancianos

print(f'El promedio de niños es {round(promedioNiño)}, el promedio de Jovenes {round(promedioJovenes)}, el promedio de adultos {round(promedioAdultos)} y el promedio de ancianos {round(promedioAncianos)}')
# Imprime los promedios de peso redondeados para cada categoría (niños, jóvenes, adultos, ancianos)
