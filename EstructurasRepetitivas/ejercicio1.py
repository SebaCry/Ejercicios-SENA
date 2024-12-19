"""Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos
neutros.

Hola instru, hice el ejercicio 1 y 2 con arrays"""

positivos = [] ## Declaro una variable tipo array (positvios) para guardar cuales son los numeros positvos 
negativos = [] ## Declaro una variable tipo array (negativos) para guardar cuales son los numeros negativos
neutros = [] ## Declaro una variable tipo array (neutros) para guardar los cuales son los numeros neutro
for i in range(0,20): ## Hago un bucle for para repetir los procesos 20 veces
    numeros = int(input('Digita los numeros💫: ')) ## Hacer una variable tipo entrada para digitar los numeros
    if numeros < 0: ## Si los numeros son menores a cero
        negativos.append(numeros) ## Dicho numero se agregara al array negativos
        cantidadNegativo = len(negativos) ## Se crea una variable con el metodo len (lenght) se muestra la cantidad de digitos que hay en el array
    elif numeros > 1: ## De lo contrario si numeros es mayor a cero  
        positivos.append(numeros) ## Dicho numero se agregara al array positivos
        cantidadPositivo = len(positivos) ## Se crea una variable con el metodo len (lenght) se muestra la cantidad de digitos que hay en el array
    elif numeros == 1 or numeros == 0: ## De lo contrario si numeros es 1 o 0
        neutros.append(numeros) ## Dicho numero se agregara al array de neutros
        cantidadNeutro = len(neutros) ## Se crea una variable con el metodo len (lenght) se muestra la cantidad de digitos que hay en el array
    else: ## De lo contrario
        print(f'Numero equivocado') ## Se imprime un mensaje de error
print(f'Los numeros positivos son {cantidadPositivo}, los negativos son {cantidadNegativo} y los numeros neutros son: {cantidadNeutro}') ## Se imprimen la cantidad de numeros que hay con la variable, cantidadPositivo, cantidadNegativo, cantidadNeutro

