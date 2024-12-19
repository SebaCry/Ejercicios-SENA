"""Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se
digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto."""

numero = int(input('Ingresa el numero a calcular de la tabla: ')) ## Se crea una variable numero para que el usuario registre que numero de la tabla quiere sacar

for i in range(1, 11): ## Se crea un bucle que recorra del 1 al 10
    print(f'Tabla del {numero} es: {numero} * {i} = {numero*i} ') ## En la impresion se hacen las operaciones. 
    #Si un usuario digita 5 entonces 5 * (por la posicion del array i = 1,2,3,4,5) y ya en el resultado se muestra la multiplicacion de ambos