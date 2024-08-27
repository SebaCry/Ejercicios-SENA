amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0
i = 0

nCarros = int(input('¿Cuantos carros entraron '))

while i < nCarros:
    placa = int(input('Ingresa tu ultima placa: '))
    if placa == 1 or placa == 2:
        amarillo += 1
    elif placa == 3 or placa == 4:
        rosa += 1
    elif placa == 5 or placa == 6:
        roja += 1
    elif placa == 7 or placa == 8:
        verde += 1
    elif placa == 9 or placa == 0:
        azul += 1
    else:
        print('Digito mal puesto :(')
    i += 1

print(f'La cantidad de carros amarillos es: {amarillo}, la de rosa {rosa}, la de rojos {roja}, la de verdes {verde} y la de azules es {azul}')

