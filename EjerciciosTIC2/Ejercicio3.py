payasos = int(input('Cuantos payasos vas a comprar?: '))
muñecas = int(input('Cuantos muñecas vas a comprar?: '))

peso_pay = 112 * payasos
peso_mun = 75 * muñecas

peso_total = peso_pay + peso_mun

print(f'El peso total del paquete es: {peso_total} g')