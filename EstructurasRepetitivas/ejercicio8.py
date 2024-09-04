"""8.un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un
algoritmo que lea por cada estudiante la calificación obtenida. Al finalizar calcule e
imprima:"""

estudiantes1 = 0  ## Se declaran diferentes variables que son contadores que iran incrementando su valor de a 1
estudiantes2 = 0
estudiantes3 = 0
estudiantes4 = 0

for estudiante in range(0,23): ## Se hace un bucle for que repetira 23 veces los procedimientos internos
    nota = int(input('¿Cual fue tu calificacion de 1 - 100?: ')) ## Se crea una variable nota que guardara la calificacion que el usuario ingrese
    if nota < 50: ## Si nota es menor a 50
        estudiantes1 += 1 ## La cantidad de estudiantes que sacaron menos de 50 incrementara 1
    elif nota >= 50 and nota < 70: ## Si nota es mayor o igual a 50 y sea menor a 70
        estudiantes2 += 1 ## La cantidad de estudiantes que sacaron mayor o igual a 50 y sea menor a 70 incrementara 1
    elif nota >= 70 and nota < 80: ## Si nota es mayor o igual a 70 y sea menor a 80
        estudiantes3 += 1 ## La cantidad de estudiantes que sacaron  mayor o igual a 70 y sea menor a 80 incrementara 1
    elif nota >= 80: ## Si nota es mayor o igual a 80
        estudiantes4 += 1 ## La cantidad de estudiantes que sacaron menos o igual de 80 incrementara 1
    else:
        print('Mala digitacion') ## Mensaje de error

print(f'Esudiantes menores a 50: {estudiantes1}\n Estudiantes mayores de 50 pero menores de 70: {estudiantes2}\n Estudiantes mayores de 70 pero menores de 80: {estudiantes3}\n Estudiantes mayores a 80: {estudiantes4}')
## Se imprimen los valores de estudiantes y las estadisticas