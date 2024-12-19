'''
Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
contraseña introducida por el usuario coincide con la
guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

contraseña = str(input('Ingresa tu contraseña: ')).lower()

contraseña_veri = str(input('Verifica tu contraseña: ')).lower()

if contraseña == contraseña_veri:
    print('Tu contraseña es correcta 👍')
else:
    print('Tu contraseña es incorrecta.')