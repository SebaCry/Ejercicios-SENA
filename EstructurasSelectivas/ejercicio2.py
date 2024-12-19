"""Calcular el total a pagar por la compra de zapatillas. Si se compran 3 o mas zapatillas se aplica un descuento del 20% sobre el total de la compra
y si son menos de 3 zapatillas un descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento y el valor a pagar 
una vez aplicado el descuento"""
##Hola instru esta es una manera peculiar de realizar el ejercicio, usando estructuras bucles.
array = [] ## Declaro un array vacio para guardar los datos de las zapatillas
zap = int(input('¿Cuantas zapatillas vas a comprar?')) ##Defino el valor de las zapatillas

for i in range(zap): ##Hago un bucle for para recorrer el array
    valueZap = int(input('Pon el valor de tus zapatillas: ')) ##Defino el valor de las zapatillas, donde se va a repetir el bucle
    array.append(valueZap) ##Agrego el valor de las zapatillas al array
    print(array) ## Imprimo el array

suma = sum(array) ## Hago una suma de todos los valores de las zapatillas

if zap < 3:##Se hace el condicional para saber si las zapatillas que compraste en menor que 3
    descuent = suma * 0.1 ## Se opera el descuento con el 20%
    valueFinal = int (suma - descuent)##Se resta el descuento con el valor base de la zapatilla
    print(f'El valor de tu compra es {suma}, el valor del descuento {descuent}, el valor a pagar es {valueFinal}')##Imprimo los diferentes valores
elif zap >= 3:##Se hace un Sino Si para sacar el descuento si con el 30%
    descuent = suma * 0.2##Se opera con el descuento del 30%
    valueFinal = int(suma - descuent) ##Hago un casteo, para que salga en numero entero, y le resto al valor base de la zapatilla 
    print(f'El valor de tu compra es {suma}, el valor del descuento {descuent}, el valor a pagar es {valueFinal}') ##Imprimo los diferentes valores
else:
    print('Numero mal digitado') ## Imprimo un mensaje de error








