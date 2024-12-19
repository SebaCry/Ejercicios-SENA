invertir = float(input('Cual es la cantidad a invertir?: '))
interes_anual = int(input('Cual es el interes anual?: '))
num_años = int(input('Por cuantos años desea invertir?: '))

op= str(round(invertir * (interes_anual / 100 + 1) ** num_años, 2))

print(f'La capital final es de {op}')