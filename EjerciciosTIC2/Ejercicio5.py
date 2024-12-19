peso = float(input('Ingresa tu peso: '))
estatura = float(input('Ingresa tu estatura: '))

imc = round((peso / estatura),2)

print(f'Tu indice de masa corporal es {imc}')