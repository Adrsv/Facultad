def Fecha():
    meses = {
        1: ('enero', 31),
        2: ('febrero', 28),
        3: ('marzo', 31),
        4: ('abril', 30),
        5: ('mayo', 31),
        6: ('junio', 30),
        7: ('julio', 31),
        8: ('agosto', 31),
        9: ('septiembre', 30),
        10: ('octubre', 31),
        11: ('noviembre', 30),
        12: ('diciembre', 31)
    }

    while True:
        dias = int(input('Ingrese el día: '))
        if dias < 1 or dias > 31:
            print('Día incorrecto. Debe estar entre 1 y 31.')
            continue
        
        mes = int(input('Ingrese el mes (1-12): '))
        if mes < 1 or mes > 12:
            print('Mes incorrecto. Debe estar entre 1 y 12.')
            continue
        
        max_dias = meses[mes][1]
        if mes == 2:
            anio = int(input('Ingrese el año: '))
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                max_dias = 29
        
        if dias > max_dias:
            print(f'Fecha {dias}/{mes} incorrecta, {mes} no tiene {dias} días.')
            continue
        
        anio = int(input('Ingrese el año: '))
        if anio > 2024:
            print(f'Año {anio} incorrecto. Debe ser 2024 o anterior.')
            continue
        
        print(f'La fecha es: {dias}/{mes}/{anio}')
        break

Fecha()