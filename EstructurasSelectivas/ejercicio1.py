"""Determinar si un aprendiz aprueba o desaprueba Algoritmia, sabiendo que aprobara si su promedio de 3 calficaciones
es mayor o igual a 70; reprueba en caso contrario (...)"""
n1 = int(input('Ingresa tu nota 1: '))##En estas 3 lineas declaro las varibles n1,n2,n3 para ingresar las notas
n2 = int(input('Ingresa tu nota 2:' ))
n3 = int(input('Ingresa tu nota 3:' ))
prom = (n1 + n2 + n3) / 3##En esta linea se opera el promedio de esas 3 notas

if prom >= 70 and prom <= 100: ##Aplico el condicional si el promedio es mayor o igual de 70 y que sea menor a 100 por el limete de nora
    print('Aprobaste bro ;)')##Aprueba la nota
else:
    print('Desaprobaste, ponte las pilas')##De lo contrario, reprueba el curso 