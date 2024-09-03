"""Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo:
(1*2*3*4*5...)."""

cont = 1 ## Se inicia un contador en uno  
for i in range(1,21): ## Se crea un bucle for de rango de 1 a 20
    cont *= i ## Ese contador se va a estar actualizando y multiplicando por el indice del bucle ejemplo = (1 * 1 = 1) -> (1 * 2 = 2) -> (2 * 3 = 6) ...
    print(cont) ## Se imprime el contador