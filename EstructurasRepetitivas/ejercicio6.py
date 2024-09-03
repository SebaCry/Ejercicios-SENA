"""Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un
total de n personas."""

nPersonas = int(input('Ingresa la cantidad de personas que asisiran: ')) ## Se crea una vairiable nPersonas que registrara la cantidad de personas que asistirar
mujeres = 0 ## Se crea un contador para las mujeres
hombres = 0 ## Se crea un contador para los hombres
i = 0 ## Se crea un indice que inicie en 0 que ira incrementando

while i < nPersonas: ## Se crea un bucle while que se repetira si i es menor a la cantidad de personas digitadas
    sex = str(input('¿Cual es tu sexo? ¿femenino || masculino?:  ')).lower() ## Se crea una variable sex, que el usuario digitara que tipo de sexo es
    if sex == 'femenino': ## Si el sexo registrado es femenino
        mujeres += 1 ## Se incrementara 1  al contador mujeres
    elif sex == 'masculino': ## De lo contrario si el sexo es masculino
        hombres += 1 ## Al contador de hombres se incrementara 1
    else: ## De lo contrario
        print('Error, pusiste un dijito equivocado') ## Se imprimira un mensaje de error
        continue ## Y el bucle continuara
    i += 1 ## Se ira incrementando el indice, para que el bucle termine cuando llegue a la cantidad de nPersonas
    
print(f'La cantidad de personas es: {nPersonas}, hay {mujeres} mujeres, y hay {hombres} hombres.') ## Se imprimira la cantidad de persoas, cuantas mujeres hay y hombres