##DEFINICIÓN VARIABLES
mensaje = 'Hola, estoy aprendiendo Python.' ; formacion = 'SENA'; nombre = 'Juan Sebastian Perez Cedano'
edad = 16 ; estatura = 1.7256 ; peso = 60 

#Forma de imprimir 1
print(mensaje,'Mi nombre es:',nombre, 'Soy de la formacion:',formacion, 'tengo:',edad,'y mi estatura es de:',"%.3f" % estatura,'Actualmente peso:',peso,'kg')
print('\n')

#Forma de imprimir 2
print(f'{mensaje}mi nombre es: {nombre} soy de la formacion:{formacion} .Tengo {edad} años, mido {estatura} y tengo un peso de: {peso} kg')
print('\n')

##DEFINIR VARIABLES Y OPERARLAS
a = int(input('Ingresa un digito: '))
b = int(input('Ingresa un digito: '))


print('-Multiplicacion=',a*b,'Division=',a//b,'Suma=',a+b,'Resta=',a-b,'Division Res=',a%b)
print(f'-Multiplicacion={a*b},Division={a//b},Suma={a+b},Resta={a-b},Division,Res={a%b}')