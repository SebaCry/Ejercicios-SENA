positivos = []
negativos = []
neutros = []
for i in range(0,20):
    numeros = int(input('Digita los numeros💫: '))
    if numeros < 0:
        negativos.append(i)
        negativo = len(negativos)
    elif numeros > 0:
        positivos.append(i)
        positivo = len(positivos)
    elif numeros == 1 or numeros == 0:
        neutros.append(i)
        neutro = len(neutros)
print(f'Los numeros positivos son {positivo}, los negativos son {negativo} y los neutros son {neutro}')

