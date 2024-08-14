"""
Calcular el numero de pulsaciones que debe tener una persona por cada 10 segundos de
ejercicio aeróbico, la formula que se aplica es: (...)
"""

import time
print('Femeninio || Masculino')
sex = str.lower(input('¿Cual es tu sexo?: '))
edad = int(input('¿Cual es tu edad?: '))

"""
pulsaciones = 0

while (pulsaciones < 15):
    pulsaciones += 1
    for i in range(1,11):
        print(f'Seg. {i}') ##Es fragmento de codigo es solo de experimentacion para contar las pulsaciones
        time.sleep(0.3)
    print(f'Pulsacion {pulsaciones}')
"""


if sex == 'femenino':
    pulsaciones = (220 - edad) / 10
    print(f'El numero de pulsaciones es: {pulsaciones}, por cada 10 segundos')
elif sex == 'masculino':
    pulsaciones = (210 - edad) / 10
    print(f'El numero de pulsaciones es: {pulsaciones}, por cada 10 segundos')
else:
    print('Escribe bien brooo')