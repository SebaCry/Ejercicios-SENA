"""11. Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa
se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio
,la cantidad de alumnos que tienen una altura mayor a 1.70 cm,"""

hombres = 0  # Contador de hombres
mujeres = 0  # Contador de mujeres
alturas = 0  # Suma de todas las alturas ingresadas
alturaMayor = 0  # Contador de personas con altura mayor a 1.70m
alturaMenor = 0  # Contador de personas con altura menor o igual a 1.50m
numAlturas = 0  # Contador de la cantidad total de alturas ingresadas

while True:  # Bucle infinito para ingresar datos hasta que se ingrese una edad de 0
    try:
        edad = int(input('¿Cuál es tu edad?: '))  # Se pide la edad al usuario
        if edad == 0:  # Si la edad es 0, se rompe el bucle
            break
        
        
        sex = input('¿Cuál es tu sexo (masculino/femenino)?: ').lower()  # Se pide el sexo y se convierte a minúsculas
        if sex == 'femenino':  # Si el sexo es femenino
            mujeres += 1  # Se incrementa el contador de mujeres
        elif sex == 'masculino':  # Si el sexo es masculino
            hombres += 1  # Se incrementa el contador de hombres
        else:
            print("Sexo no válido. Por favor, ingresa 'masculino' o 'femenino'.")  # Mensaje de error si el sexo no es válido
            continue  # Salta al siguiente ciclo del bucle

        altura = float(input('¿Cuál es tu altura?: '))  # Se pide la altura al usuario
        if altura <= 0:  # Si la altura es menor o igual a 0
            print("Por favor, ingresa una altura válida.")  # Mensaje de error si la altura no es valida
            continue  # Salta al siguiente ciclo del bucle
        
        alturas += altura  # Se suma la altura ingresada al total de alturas
        numAlturas += 1  # Se incrementa el contador de alturas ingresadas
        if altura > 1.70:  # Si la altura es mayor a 1.70
            alturaMayor += 1  # Se incrementa el contador de alturas mayores a 1.70
        elif altura <= 1.50:  # Si la altura es menor o igual a 1.50m
            alturaMenor += 1  # Se incrementa el contador de alturas menores o iguales a 1.50
    
    except ValueError:  # Si hay un error de valor
        print("Entrada no válida. Asegúrate de ingresar números correctos.")  # Mensaje de error
        continue  # Salta al siguiente ciclo del bucle

if numAlturas > 0:  # Si se ingresaron alturas
    promAltura = alturas / numAlturas  # Se calcula la altura promedio
    print(f'La cantidad de hombres es: {hombres}, la de mujeres es: {mujeres}, la altura promedio es: {promAltura:.2f}')  # Se imprimen los resultados
else:  # Si no se ingresaron alturas
    print(f'La cantidad de hombres es: {hombres}, la de mujeres es: {mujeres}. No se ingresaron alturas.')  # Se imprime un mensaje indicando que no hay alturas


