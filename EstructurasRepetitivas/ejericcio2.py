"""Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
números."""

numeros = [] ##Se crea una variable tipo array para guardar todos los numeros negativos
numerosNeg = [] ## Se crea
for i in range(0,3):
    numNeg = float(input('Digita 10 numeros negativos: '))
    numeros.append(numNeg)

    if numeros[i] < 0:
        neg = numeros[i] * -1
        numerosNeg.append(neg)
        suma = sum(numerosNeg)
    else:
        print('Coloca un numero positivo')

print(f'Los numeros convertidos son {numerosNeg} La suma de los numeros es igual a: {suma}')
