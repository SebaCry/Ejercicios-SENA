"""En una llantera se ha establecido una promocion de las llantas marca 'Todo terreno', dicha promocion consisten en lo siguinte:
Si se comprar menos de 5 llantas el precio es de 300.000"""

llantas = int(input('¿Cuantas llantas vas a comprar?: '))

if llantas < 5:
    llantas *= 300000
    print(f'Esto de cuestan las llantas si compras menos de 5: {llantas}')
elif llantas >= 5 and llantas <= 10:
    llantas *= 250000
    print(f'Esto te cuestan las llantas si compras mas de 5 hasta 10: {llantas}')
elif llantas > 10:
    llantas *= 200000
    print(f'Precio de las llantas si compras mas de 10: {llantas}')
else:
    print('Digita bien el numero')