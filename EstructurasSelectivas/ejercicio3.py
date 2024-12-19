"""Una empresa quiere hacer una compra de varias piezas de la misma clase a una fabrica de bolsos. La empresa, dependiendo del monto total de la compra,
decidira que hacer para pagar al fabricante (...)"""

montoTotal = int(input('Ingresa tu monto total: ')) ##Se declara la variable "montoTotal" tipo int

if montoTotal > 500000: ##Se hace un condicional para saber si el monto total es mayor a 500000
    inversion = int (montoTotal * 0.55)  ## Asi mismo la variable "inversion" se declara tipo int, y se opera con el porcentaje, hago un casteo a la variable "inversion"
    prestamos = int (montoTotal * 0.3) ## Declaro los prestamos, multiplicanto mi montoTotal un 30 %
    restanteCredito = int (montoTotal * 0.15) ##Asi mismo desclaro restanteCredito para sacar el descuento del 15%
    print(f'Su monto total es de: {montoTotal} Valor invertido {inversion}, el valor prestado al banco es de: {prestamos} y el valor del credito del fabricante es {restanteCredito}') ##Imprimo los diferentes valores
elif montoTotal < 500000: ##Si el montoTotal es menor a 500000
    inversion = int (montoTotal * 0.7) ##Se declara la inversion y se le saca el porcentaje del 70%
    credito = int (montoTotal * 0.3) ## Se declara credito y se le saca el porcentaje del 30%
    intereses = int (credito * 0.2) ## Se declara intereses y se le saca el porcentaje del 20%
    credito += intereses ## Se le suman los intereses
    print(f'Su monto total es de: {montoTotal} Valor invertido: {inversion}, valor de credito al fabricante {credito} (A el credito se le cobran estos intereses {intereses})') ## Imprimo los diferentes valores
else:
    print('Te equivocaste')  
    

