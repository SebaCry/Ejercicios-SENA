"""Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos."""

mujeres = 0  ##Se inicializan 2 contadores (mujeres, hombres) y 2 (edadMujer, edadHombre)acumuladores 
hombres = 0
edadMujer = 0
edadHombre = 0

personas = int(input('¿Cuantas personas hay en el salon?: ')) ## Se declara una variable personas que digitara cuantas personas hay en el salon

for persona in range(personas): ## Se crea un bucle for que recorrera el rango de personas (lo que digito el usuario)
    sex = str(input('¿Cual es tu sexo? ¿femenino || masculino?: ')).lower() ## Se crea una variable sex que el usuario digitara si es femenino o masculino 
    edad = int(input('¿Cual es tu edad?: ')) ##  Se crea una variable que preguntara cual es la edad
    
    if sex == 'femenino': ## Si sex es femenino
        mujeres += 1 ## A mujeres se le incrementara 1
        edadMujer += edad ## En el acumulador, se sumaran las edades que digite el usuario
    elif sex == 'masculino': ## De lo contrario si el sex es masculino 
        hombres += 1 ## Se incrementara 1 a hombres
        edadHombre += edad ## Al acumulador, se le sumaran las edades totales
    else:
        print('Ingresa un valor valido') ## Imprime un mensaje de error

promMujer = edadMujer / mujeres ## Se halla el promedio de las edades de mujeres
promHombre = edadHombre / hombres ## Se halla el promedio de las edades de hombres
promedioTotal = (edadHombre + edadMujer) / (mujeres + hombres) ## Se halla el promedio general de todos los alumnos

print(f'El promedio de mujeres es: {promMujer}, el promedio de hombres es: {promHombre}, y el promedio total es: {promedioTotal}')
## Se imprimen los diferentes promedios.