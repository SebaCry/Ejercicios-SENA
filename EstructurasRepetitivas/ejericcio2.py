"""Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
números."""

numerosNeg = [] ##Se crea una variable tipo array para guardar todos los numeros negativos
numerosConver = [] ## Se crea una variable para guardar los numeros convertidos
for i in range(0,10): ##Se crea un bucle de 0 a 20 que va a repetir lso procedimientos 20 veces
    numNeg = float(input('Digita 10 numeros negativos: ')) ## Se crea una variable para digitar los numeros
    numerosNeg.append(numNeg) ## Al array numerosNeg se van agregar todos los numeros digitados   

    if numerosNeg[i] < 0: ## Si en cada posicion del array es menor a 0
        neg = numerosNeg[i] * -1 ## Se crea una variable que va a guardar los numeros convertidos, multiplicandolos por -1
        numerosConver.append(neg) ## Al array numerosConver se le agregaran los numeros convertidos
        suma = sum(numerosConver) ## Se suman todos los digitos del array de los numeros convertidos
    else: ## De lo contrario
        print('Coloca un numero negativo') ## Se imprime un mensaje de error

print(f'Los numeros convertidos son {numerosConver} La suma de los numeros es igual a: {suma}')
