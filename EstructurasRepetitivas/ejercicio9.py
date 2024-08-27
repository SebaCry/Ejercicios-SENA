mujeres = 0
hombres = 0
edadMujer = 0
edadHombre = 0

personas = int(input('¿Cuantas personas hay en el salon?: '))

for persona in range(personas):
    sex = str(input('¿Cual es tu sexo? ¿femenino || masculino?: ')).lower()
    
    
    if sex == 'femenino':
        mujeres += 1
        edad = int(input('¿Cual es tu edad?: '))
        edadMujer += edad
    elif sex == 'masculino':
        hombres += 1
        edad = int(input('¿Cual es tu edad?: '))
        edadHombre += edad
    else:
        print('Ingresa un valor valido')
promMujer = edadMujer / mujeres
promHombre = edadHombre / hombres 
sumaTotal = (edadHombre + edadMujer) / (mujeres + hombres)

print(f'El promedio de mujeres es: {round(promMujer)}, el promedio de hombres es: {round(promHombre)}, y el promedio total es: {round(sumaTotal)}')