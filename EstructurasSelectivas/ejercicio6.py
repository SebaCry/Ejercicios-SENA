"""Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: Si el promedio obtenido por un alumno
en el ultimo periodo es mayor o igual que 4.0, se le hará un descuento del 30% sobre la pension (...)"""

nombre = str(input('Ingrese el nombre del estudiante: ')) ##Delcaro la variable nombre, para que el usuario registre el nombre
pension = float(input('¿Cuanto paga por pension?: ')) ## Delcaro la variable pension, para que el usuario registre el valor de la pension
promedio = float(input('Ingresa el promedio general obtenido: ')) ## Delcaro la variable promedio, para que el usuario registre el promedio

if promedio >= 4.0 and promedio <= 5.0: ## Si el promedio es mayor o igual que 4.0 y menor o igual que 5.0
    pension *= 0.3 ## Se le aplica un descuento del 30%
    print(f'Al estudiante {nombre}, se le descuenta un 30% a la pension, por lo cual este seria el pago final {"%.0f" % pension}') ## Se imprime el valor de la pension junto al nombre del estudiante, y tambien aplicando el formato para que solo muestre el valor entero
elif promedio < 4.0 and promedio > 0.0: ## De lo contrario, si el promedio es menor que 4.0 y mayor que 0.0
    iva = pension * 0.1 ## Solo se le aplica el iva
    pension += iva ##Sumandole este a la pension
    print(f'Al estudiante {nombre}, debera pagar la pension completa con el iva {"%.0f" % pension} ') ## Se imprime el valor de la pension junto al nombre del estudiante
else:
    print('Ingresa un numero valido <:') ## Imprimo un mensaje de error