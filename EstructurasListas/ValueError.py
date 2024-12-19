"""
Excepciones Comunes en Python

    -ZeroDivisionError: Ocurre cuando se intenta dividir un número por cero.
    -Ejemplo: result = 10 / 0

    -IndexError: Se produce cuando se intenta acceder a un índice que está fuera del rango de una lista.
    -Ejemplo: my_list = [1, 2, 3]; print(my_list[5])

    -KeyError: Ocurre cuando se intenta acceder a una clave que no existe en un diccionario.
    -Ejemplo: my_dict = {'a': 1}; print(my_dict['b'])

    -TypeError: Se lanza cuando se realiza una operación o función en un tipo de dato inapropiado.
    -Ejemplo: result = '2' + 2

    -ValueError: Ocurre cuando una operación o función recibe un argumento del tipo correcto pero con un valor inapropiado.
    -Ejemplo: int("not a number")

    -FileNotFoundError: Se produce al intentar abrir un archivo que no existe.
    -Ejemplo: with open('non_existent_file.txt') as f: pass

    -NameError: Ocurre cuando se intenta acceder a una variable que no ha sido definida.
    -Ejemplo: print(undefined_variable)

    -ModuleNotFoundError: Se lanza cuando se intenta importar un módulo que no se encuentra.
    -Ejemplo: import non_existent_module

    -AttributeError: Ocurre cuando se intenta acceder a un atributo que no existe en un objeto.
    -Ejemplo: my_list = [1, 2, 3]; my_list.append(4).non_existent_method()

    -EOFError: Se produce cuando se alcanza el final de un archivo de entrada sin leer datos.
    -Ejemplo: input() cuando no hay más datos disponibles.

"""