while True:
    print('1. Pan no del dia\n')
    print('2. Pan del dia\n')
    print('3. No quiero comprar pan\n')
    tipo_pan = int(input('Que tipo de pan va a comprar?: '))

    if tipo_pan == 1:
        panes = int(input('Cuantos panes vas a comprar?: '))
        pan_desc = (panes * 3.49) * 0.6
        print(f'El coste final a pagar es: {pan_desc} euros con descuento aplicado del 60%')
    elif tipo_pan == 2:
        panes = int(input('Cuantos panes vas a comprar?: '))
        pan_normal = panes * 3.49
        print(f'El coste final a pagar es: {pan_normal} euros')
    elif tipo_pan == 3:
        print('Hasta luego')
        break
    else:
        print('Ingresa un codigo correcto')
        continue