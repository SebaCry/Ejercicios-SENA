"""Una persona debe realizar un muestreo con 50 personas para determinar el
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona.
Las categorías se determinar de acuerdo a la siguiente tabla:"""

pesoNiño = 0
pesoJoven = 0
pesoAdulto = 0 
pesoAnciano = 0

niños = 0
adultos = 0
jovenes = 0
ancianos = 0

promedioNiño = 0
promedioJovenes = 0
promedioAdultos = 0
promedioAncianos = 0

for i in range (1, 51): ## Se crea un bucle for que repita los procedimientos 50 veces
    edades = int(input('Ingresa tu edad: ')) ## Se crea una variable edades que guardara las edades
    pesos = int(input('Ingresa tu peso: ')) ## Una variable pesos, que guardara los pesos digitados

    if 0 <= edades <= 12: ## Si las edades son mayores a 0 y menores a 12
        niños += 1 ## Se le sumara 1 al contador niños
        pesoNiño += pesos 
        promedioNiño = pesoNiño / niños ##
    elif 13 <= edades <= 29: ## De lo contrario, si edades es mayor a 13 y edades es menor a 29
        jovenes += 1 ## Se le sumara 1 al contador jovenes
        pesoJoven += pesos
        promedioJovenes = pesoJoven / jovenes
    elif 30 <= edades <= 59: ##De lo contrario, si edades es mayor a 30 y edades es menor 
        adultos += 1 ## Se le sumara 1 al contador de adultos
        pesoAdulto += pesos
        promedioAdultos = pesoAdulto / adultos ## Al peso adulto se le sumara los pesos que se le asignen
    elif edades >= 60: ## De lo contrario si edades es mayor o igual a 60
        ancianos += 1 ## Se le sumara 1 al contador de ancianos
        pesoAnciano += pesos
        promedioAncianos = pesoAnciano / ancianos
    else:
        print('Digito mal puesto')


print(f'El promedio de niños es {round(promedioNiño)}, el promedio de Jovenes {round(promedioJovenes)}, el promedio de adultos {round(promedioAdultos)} y el promedio de ancianos {round(promedioAncianos)} ')
## Se imprimen los valores de cada individuo