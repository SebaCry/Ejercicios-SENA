"""En una llantera se ha establecido una promocion de las llantas marca 'Todo terreno', dicha promocion consisten en lo siguinte:
Si se comprar menos de 5 llantas el precio es de 300.000"""

llantas = int(input('¿Cuantas llantas vas a comprar?: ')) ## Delcaro la variable llantas, para que el usuario registre el valor de las llantas

if llantas < 5: ## Si las llantas son menores a 5
    llantas *= 300000 ## El precio de cada una de las llantas es de 300.000, y por eso se multiplican
    print(f'Esto de cuestan las llantas si compras menos de 5: {llantas}') ## Se imprime el valor de las llantas
elif llantas >= 5 and llantas <= 10: ## Sino, si las llantas son entre 5 y 10
    llantas *= 250000 ## El precio de cada una de las llantas es de 250.000, por eso de multiplican
    print(f'Esto te cuestan las llantas si compras mas de 5 hasta 10: {llantas}') ## Se imprime el valor de las llantas
elif llantas > 10: ## Sino, si las llantas son mas de 10
    llantas *= 200000 ## El precio de cada una de las llantas es de 200.000, por eso de multiplican 
    print(f'Precio de las llantas si compras mas de 10: {llantas}') ## Se imprime el valor de las llantas
else:
    print('Digita bien el numero') ## Imprimo un error