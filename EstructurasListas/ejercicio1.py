## -----------------------------------------------Listas---------------------------------------------------
aprendices = []
edades = []


nStudents = int(input('Cuantos estudiantes hay?: '))
i = 0

while i < nStudents:
    datesNames = str(input('Ingresa tu nombre: ')).lower().strip()
    datesAges = int(input('Ingresa tu edad: '))

    aprendices.append(datesNames)
    edades.append(datesAges)

    i += 1

print(aprendices)
print(edades)
print(' ')
##---------------------------------------------------------------------------------------------------------
edadMaxima = max(edades)
print(f'El estudiante {aprendices[0]} con su edad de {edadMaxima} es el estudiante con mayor edad')
print(' ')
##----------------------------------------------------------------------------------------------------------
aprendices.insert(0, 'Sandra Milena Cruz')
print(f'Al grupo se le va anadir la instructora Sandra: {aprendices}')
print(' ')
#-----------------------------------------------------------------------------------------------------------
contadorAprendices = edades.count(18)
print(f'Hay {contadorAprendices} estudiantes con 18 anos')
print(' ')
#-----------------------------------------------------------------------------------------------------------
aprendizExtra = 'Sara Rodriguez'
aprendices.append(aprendizExtra)
print(f'Se le agrega la aprendiz Sara al grupo de aprendices: {aprendices}')
print(' ')
#-----------------------------------------------------------------------------------------------------------

aprendices.pop(0)
print(f'Se elimina la primera persona del grupo (osea la instru, perdon instru): {aprendices}')
print(' ')
#-----------------------------------------------------------------------------------------------------------
datoABuscar = aprendices.index('reyes')
print(f'El joven reyes esta en el indice: {datoABuscar}')
print(' ')
#-----------------------------------------------------------------------------------------------------------

print(f'Los primeros 10 aprendices de la lista son: {aprendices[0:10]}')
print(' ')
#-----------------------------------------------------------------------------------------------------------

print(f'Los ultimos 10 aprendices de la lista: {aprendices[-1: -11: -1]}')
print(' ')
#-----------------------------------------------------------------------------------------------------------

print(f'Los aprendices del 10 a 20 son: {aprendices[10:20]}')
print(' ')
#-----------------------------------------------------------------------------------------------------------

print(f'Los aprendices con el indice par son: {aprendices[0:nStudents:2]}')