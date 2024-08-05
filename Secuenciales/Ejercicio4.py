nombreVendedor = str(input('Ingresa tu nombre: '))##Declaro la variable nombreVendedor como texto, para que el usuario lo coloque
sueldoVendedor = int(input('Ingresa tu sueldo: '))##Declaro la variable sueldoVendedor como entero, para que el usuario lo coloque
valorComision = int(input('Ingresa tus comisiones: '))##Declaro la variable valorComision como entero, para que el usuario lo coloque
sueldoFinal = sueldoVendedor + valorComision##Declaro una variable sueldoFinal para colocar el sueldo final con la comision de venta 

print(f'El vendedor {nombreVendedor}, tiene un sueldo de {sueldoVendedor}, durante el mes obtuvo una comision de{valorComision}\nEl valor final de su sueldo es de: {sueldoFinal}')
##Finalmente imprimo en mi consola, el texto que explique el nombre del vendedor, su sueldo, la comision del mes y su sueldo final