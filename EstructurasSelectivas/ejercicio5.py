"""
Calcular el numero de pulsaciones que debe tener una persona por cada 10 segundos de
ejercicio aeróbico, la formula que se aplica es: (...)
"""

##import time ## Hola instru, quise importar la libreria time para hacer una pausa, pero es como experimento
print('Femeninio || Masculino') ##Defino si el el usuario es femenino o masculino
sex = input('¿Cual es tu sexo?: ').lower().strip() ##Declaro una variable sex para saber si el usuario es femenino o masculino
edad = int(input('¿Cual es tu edad?: ')) ##Asi mismo, una variable edad para saber la edad

"""
pulsaciones = 0

while (pulsaciones < 15):
    pulsaciones += 1
    for i in range(1,11):
        print(f'Seg. {i}') ##Es fragmento de codigo es solo de experimentacion para contar las pulsaciones
        time.sleep(0.3)
    print(f'Pulsacion {pulsaciones}')
"""


if sex == 'femenino': ## Si el usuario es femenino
    pulsaciones = (220 - edad) / 10 ##Entonces el numero de pulsaciones es (220 - la edad) / 10
    print(f'El numero de pulsaciones es: {pulsaciones}, por cada 10 segundos') ## Imprimo el numero de pulsaciones
elif sex == 'masculino': ## Si el usuario es masculino
    pulsaciones = (210 - edad) / 10 ## Entonces el numero de pulsaciones es (210 - la edad) / 10
    print(f'El numero de pulsaciones es: {pulsaciones}, por cada 10 segundos') ## Imprimo el numero de pulsaciones
else:
    print('Escribe bien brooo') ##Doy un mensaje de error para que el usuario escriba bien