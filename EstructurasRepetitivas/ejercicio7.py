amarillo = 0 ## ## A las variables amarillo, rosa, roja, verde y azul se les inicializa con 0, ya que seran contadores para ver cuantos hay
rosa = 0
roja = 0
verde = 0
azul = 0
i = 0 ## Se crea un indice que inicie en 0 que ira incrementando

nCarros = int(input('¿Cuantos carros entraron ')) ## Se crea una variable nCarros que el usuario digite cuantos carros entraron

while i < nCarros: ## Se hace un bucle while que repetira instrucciones si i es menor que la cantidad de nCarros
    placa = int(input('Ingresa el ultimo  digito de tu placa: ')) ##Se crea una variable placa, que ingresa el ultimo digito de la placa 
    if placa == 1 or placa == 2: ## Si la placa es 1 o 2 
        amarillo += 1 ## El carro es amarillo y se le incrementara 1
    elif placa == 3 or placa == 4:## Si la placa es 3 o 4
        rosa += 1 ## El carro es rosa y se le incrementara 1
    elif placa == 5 or placa == 6:## Si la placa es 5 o 6
        roja += 1 ## El carro es roja y se le incrementara 1
    elif placa == 7 or placa == 8:## Si la placa es 7 o 8
        verde += 1 ## El carro es verde y se le incrementara 1
    elif placa == 9 or placa == 0:## Si la placa es 9 o 9
        azul += 1 ## El carro es azul y se le incrementara 1
    else:
        print('Digito mal puesto :(') ## Se imprime un mensaje de error sin o cumple las condiciones
    
    i += 1 ## Se ira incrementado el indice 1 hasta que llegue a la cantidad de carros

print(f'La cantidad de carros amarillos es: {amarillo}, la de rosa {rosa}, la de rojos {roja}, la de verdes {verde} y la de azules es {azul}') ## Se imprimen las cantidades de carros

