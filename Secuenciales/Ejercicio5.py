print('Tu producto tiene un descuento del 20%')
compra = int(input('Ingresa el coste de tu compra: '))
descuento = compra * 0.2
print(f'La compra fue{compra}, con un descuento de{descuento}')
compra -= descuento
print(f'El valor final a pagar es: {compra}')
