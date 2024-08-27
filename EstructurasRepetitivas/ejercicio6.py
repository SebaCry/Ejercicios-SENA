nPersonas = int(input('Ingresa la cantidad de personas que asisiran: '))
mujeres = 0
hombres = 0
i = 0

while i < nPersonas:
    sex = str(input('¿Cual es tu sexo? ¿femenino || masculino?:  ')).lower()
    if sex == 'femenino':
        mujeres += 1
    elif sex == 'masculino':
        hombres += 1
    else:
        print('Error, pusiste un dijito equivocado')
        continue
    i += 1
    
print(f'La cantidad de personas es: {nPersonas}, hay {mujeres} mujeres, y hay {hombres} hombres.')