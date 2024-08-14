
def obtenerEdad():
    tipoEdad = input('¿Eres un bebe, niño o adulto?: ').lower().strip()
    return tipoEdad

def imprimirEdad(tipoEdad):
    if tipoEdad == 'bebe':
        edad = int(input('¿Cuantos meses tienes?: '))
    elif tipoEdad == 'niño':
        edad = int(input('¿Cuantos años tienes?: '))
    elif tipoEdad == 'adulto':
        edad = int(input('¿Cuantos años tienes?: '))
    return edad

def obtenerSexo():
    sexo = input('¿Cual es tu sexo?: ').lower().strip()
    return sexo

def diccionarioRangos(tipoEdad, edad, sexo):
    rangosHemo = {
        'bebe':{
            '0,1' : (13,16),
            '1,6' : (10, 18),
            '6,12': (11,15)        
        },
        'niño':{
            '1,5' : (11.5, 15),
            '5,10': (12.6, 15.5),
            '10,15': (13, 15.5)
        },
        'adulto':{
            'femenino' : (12, 16),
            'masculino': (14, 18)
        }
    }

    if tipoEdad == 'adulto':
        rangoHemo = rangosHemo[tipoEdad][sexo]
    else:
        for rango, valores in rangosHemo[tipoEdad].items():
            rango_min , rango_max = map(int, rango.split(','))
            if edad >= rango_min and edad <= rango_max:
                rangoHemo = valores
                break 
    
    return rangoHemo

def imprimirHemoglobina(rangoHemo, hemoglobina):
    if hemoglobina < rangoHemo[0] or hemoglobina > rangoHemo[1]:
        print('Positivo para anemia, lo sentimos 😥')
    else:
        print('Negativo para hemoglobina 😉')

def main():
    tipoEdad = obtenerEdad()
    edad = imprimirEdad(tipoEdad)
    sexo = obtenerSexo()
    rangoHemo = diccionarioRangos(tipoEdad, edad, sexo)
    hemoblogina = float(input('¿Cual es tu rango de hemoglobina actual?🤨: '))
    imprimirHemoglobina(rangoHemo, hemoblogina)

if __name__ == '__main__':
    main()

