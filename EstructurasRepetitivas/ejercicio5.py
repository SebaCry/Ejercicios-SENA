peso = 0
niños = 0
adultos = 0
jovenes = 0
ancianos = 0

for i in range (1, 50):
    edades = int(input('Ingresa tu edad: '))
    pesos = int(input('Ingresa tu peso: '))
    peso += pesos
    if edades > 0 and edades < 12:
        niños += 1
    elif edades > 13 and edades < 29:
        jovenes += 1
    elif edades > 30 and edades < 59:
        adultos += 1
    else:
        ancianos += 1

promedio = peso / 50

print(f'La cantidad de niños es esta {niños}, de ancianos es esta {ancianos} la cantidad de jovenes es esta {jovenes} y finalmente, los adultos son {adultos} \n Y el promedio de pesos es igual a: {promedio}')
