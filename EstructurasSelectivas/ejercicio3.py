"""Una empresa quiere hacer una compra de varias piezas de la misma clase a una fabrica de bolsos. La empresa, dependiendo del monto total de la compra,
decidira que hacer para pagar al fabricante (...)"""

montoTotal = int(input('Ingresa tu monto total: '))

if montoTotal > 500000:
    inversion = int (montoTotal * 0.55)
    prestamos = int (montoTotal * 0.3)
    restanteCredito = int (montoTotal * 0.15)
    print(f'Valor invertido {inversion}, el valor prestado al banco es de: {prestamos} y el valor del credito del fabricante es {restanteCredito}')
elif montoTotal < 500000:
    inversion = int (montoTotal * 0.7)
    credito = int (montoTotal * 0.3)
    intereses = int (credito * 0.2)
    credito += intereses
    print(f'Valor invertido: {inversion}, valor de credito al fabricante {credito} (A el credito se le cobran estos intereses {intereses})')
else:
    print('Te equivocaste')  
    

