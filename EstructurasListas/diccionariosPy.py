from datetime import datetime

computadores = {}

Ids = int(input('Cuantos IDs quieres agregar?: '))

def agregarEquiposId():
    for i in range(1,Ids + 1): 
        nuevoID = {}
        idComputador = int(input('Ingrese el ID del computador: '))
        nombreDispositivo = str(input('Ingrese el dispositivo: '))

        idDuplicados = [(comp['ID'],comp['DISPOSITIVOS']) for comp in computadores.values()]

        idExiste = any(idComputador == compId for compId,_ in idDuplicados)
        nombreExiste = any(nombreDispositivo == compName for _,compName in idDuplicados)

        if idExiste or nombreExiste:
            print('El ID o el dispositivo esta duplicado')
            continue
        else:
            nuevoID['ID'] = idComputador
            nuevoID['DISPOSITIVOS'] = nombreDispositivo
            computadores[i] = nuevoID

    print(computadores)

def agregarNovedades():
    for i in range(1, Ids + 1):
        novedades = {}

        fecha = input('Ingrese la fecha aaaa/mm/dd: ')
        fechaF = datetime.strptime(fecha, '%Y/%m/%d').strftime('%d-%m-%Y')

        novedades['FECHA'] = fechaF
        novedades['DESCRIPCION'] = str(input(f'Describe tu dispositivo {i}: '))

        if 'NOVEDADES' not in computadores[i]:
            computadores[i]['NOVEDADES'] = []
        
        computadores[i]['NOVEDADES'].append(novedades)

    print(computadores)

def quitarEquipos():
    eliminados = int(input('Cual ID quieres eliminar (Recuerda que van secuencialmente 1 -> 2 -> 3 ...) '))
    for i in range(1, Ids + 1):
        if eliminados == computadores[i]:
            pcEliminado = computadores.pop(i)
    
    print(f'El pc {pcEliminado} se ha eliminado de la base de datos de pc\n')

print(f'Los computadores actuales son: {computadores}')



agregarEquiposId()
agregarNovedades()
quitarEquipos()


"""
{
    1: 
    {'ID': 123, 
    'DISPOSITIVOS': 'asus', 
    'NOVEDADES': [{'FECHA': '05-12-2008', 'DESCRIPCION': 'Un computador asus del ano 2008, con 16 de ram'}]
    }, 
    
    2: 
    {'ID': 124, 
    'DISPOSITIVOS': 'hp', 
    'NOVEDADES': [{'FECHA': '06-11-2001', 'DESCRIPCION': 'Un computador hp de alta gama'}]
    }
}


"""





