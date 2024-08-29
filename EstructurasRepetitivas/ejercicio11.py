hombres = 0
mujeres = 0
alturas = 0
alturaMayor = 0
alturaMenor = 0
numAlturas = 0


while True:
    edad = int(input('¿Cual es tu edad?: '))
    if edad == 0:
        break
    
    sex = str(input('¿Cual es tu sexo?: ')).lower()
    if sex == 'femenino':
        mujeres += 1
    elif sex == 'masculino':
        hombres += 1
    
    
    altura = float(input('¿Cual es tu altura?: '))
    alturas += altura
    numAlturas += 1
    if altura > 1.70:
        alturaMayor += 1
    elif altura <= 1.50:
        alturaMenor += 1
    
    

if numAlturas > 0:
    promAltura = alturas / numAlturas
    print(f'La cantidad de hombres es: {hombres}, la de mujeres es: {mujeres}, la altura promedio es: {promAltura}')
else:
    print(f'La cantidad de hombres es: {hombres}, la de mujeres es: {mujeres}. No se ingresaron alturas.')


