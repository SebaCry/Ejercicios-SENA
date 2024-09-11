documentosPersona = [] ##Se crea una lista que guarde todos los documentos de las personas
nombresPersona = [] ## Se crea una lista para guardar todos los nombres de las personas
contadorPersonas = 0 # Se crea un contador de cuantas personas comprar
cantidadBoletas = 10 ## Se crea un acumulador decreciente 
maxCompraPorPersona = 4 ## Se crea un maximo de cuantas boletas pueden comprar


while True: ## Se crea un bucle infinito para hacer los diferentes procedimientos
    try: ## Se usa la estructura try-except para asegurar un poco las validaciones
        print('DEPORTES TOLIMA VS AMERICA DE CALI\n') ## Se imprime un mensaje de un partido de futbol 
        cuestionInicial = str(input('Quieres ingresar al partido? Si o No: ')).lower() ## Se pregunta a traves de una variable para ver si ingresan al partido
        
        if cuestionInicial == 'no': ## Si la respuesta es no
            break ## Sale del bucle y se cierra el programa

        if cuestionInicial == 'si': ## Si la respuesta es si
            contadorPersonas += 1 ## Se le incrementa 1 al contador de personas
            cuestionNombre = str(input('Ingrese su nombre completo: ')) ## Se pregunta el nombre completo de la persona
            cuestionDocumento = str(input('Ingresa tu numero de identidad: ')) ## Se le pregunta el documento completo a la personas
            
            if cuestionDocumento in documentosPersona and cuestionNombre in nombresPersona: ## Se valida con anterioridad si tanto el documento o como el nombre estan en las listas
                print('El documento esta duplicado o el nombre esta duplicado\n') ## Se imprime un mensaje de error si ya esta registrado el nombre o el documento repetido
            else: ## De lo contrario
                print(f'Hay {cantidadBoletas} disponibles') ##Se imprime el mensaje de cuantas boletas hay
                cuestionCompra = int(input('Cuantas boletas vas a comprar?: ')) ## Asi mismo se crea una variable entera para saber cuantas boletas va a commprar 
                if cuestionCompra > 0 and cuestionCompra <= 4: ## Si las boletas registradas es mayor a 0 y menor o igual 4
                    cantidadBoletas -= cuestionCompra ## Se le resta a la cantidad inicial de boletas predeterminadas
                    print(f'Has comprado {cuestionCompra} boletas.\n') ## Se imprime un mensaje de cuantas boletas se comprp
                else:
                    print('Lo maximo que puedes comprar es de 4 boletas por persona\n') ## De lo contrario, es imprimir un mensaje de error
                    continue ## El continue vuelve a hacer el bucle
        
        documentosPersona.append(cuestionDocumento) ## Ya despues de la validacion, se agrega el documento a la lista de documentos
        nombresPersona.append(cuestionNombre) ## Ya despues de la validacion se agrega el nombre a la lista de nombres

        if cantidadBoletas == 0: ## Si la cantidad de boletas llega a 0
            print('La boletas se acabaron') ## Se imprime el informe
            print(f'La personas que compraron hoy fueron: {contadorPersonas}') ## Las personas que compraron
            for documentos, nombres in zip(documentosPersona, nombresPersona): ## Se crea un formato zip para agrupar los nombres junto a sus documentos
                print(f'Esta es la lista general de personas y documentos {(documentos,nombres)}')
            break ## Se sale del bucle

    except ValueError and AttributeError and TypeError: ## Con el except del mensaje ValueError
        print('Ingresa numeros validos\n') ## Imprime el mensaje de error
        continue ## Continua con el bucle









