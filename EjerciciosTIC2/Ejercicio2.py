cant_dine = float(input('Ingresa la cantidad de dinero depositada en tu cuenta: '))
interes = cant_dine * 0.04

balance1 = round(cant_dine + interes, 2)
balance2 = round(balance1 + (1+interes),2)
balance3 = round(balance2 + (1+interes),2)

print(f'''- Balance del primer año: {balance1}
- Balance del primer año: {balance2}
- Balance del primer año: {balance3}
''')