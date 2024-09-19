''' La universidad requiere un programa para organizar las aulas para los alumnos de primer
año, de acuerdo al número de día, sabiendo que 1 es lunes y 6 es sábado.
a. Aulas: Desarrollar un programa que permita ingresar el número de día entre 1 y 6. Los
días cuyo número de orden son pares los alumnos cursan en el aula A-300,
mientras que aquellos días impares cursan en el aula A-315.
b. Descuento: Además se requiere un programa que otorgue un descuento especial del
25% en el valor de la cuota a aquellos alumnos que deseen cursar en el turno Tarde y
se inscriban a más de 3 materias, para el resto de los casos el descuento será de un
5%. El programa debe imprimir el valor de la cuota con descuento de acuerdo al caso.
c. Estacionamiento: También se requiere que el programa asigne un costo diario de
estacionamiento de $ 300 a aquellos alumnos que vengan en auto o en moto y de $ 50
si vienen en bicicleta.'''

# variables constantes
COSTO_CUOTA = 10000
DESCUENTO_MAS3 = 0.25
DESCUENTO_MENOS3 = 0.05
COSTO_ESTACIONAMIENTO_AUTO_MOTO = 300
COSTO_ESTACIONAMIENTO_BICI = 50

# Aula
while True:
    dia = int(input('Ingrese el número del día: 1 (lunes) a 6 (sábado): '))
    if 1 <= dia <= 6:
        aula = "A-300" if dia % 2 == 0 else "A-315"
        break
    else:
        print('Número o día incorrecto, vuelva a intentarlo')

# Turno
while True:
    turno = input('Ingrese el turno (Mañana, Tarde, Noche): ').strip().lower()
    if turno in ['mañana', 'tarde', 'noche']:
        break
    else:
        print(f'Turno {turno} es incorrecto, vuelva a intentarlo')

# Materias y cálculo de descuento
while True:
    materias = int(input('Ingrese la cantidad de materias: '))
    if materias > 0:
        descuento = DESCUENTO_MAS3 if materias > 3 and turno == "tarde" else DESCUENTO_MENOS3
        cuota_con_descuento = COSTO_CUOTA * (1 - descuento)
        break
    else:
        print('Debe inscribirse a al menos 1 materia')

# Estacionamiento
while True:
    vehiculo = input('Ingrese el vehículo en el que ingresa (auto, moto, bicicleta): ').strip().lower()
    if vehiculo in ['auto', 'moto', 'bicicleta']:
        costo_estacionamiento = COSTO_ESTACIONAMIENTO_BICI if vehiculo == 'bicicleta' else COSTO_ESTACIONAMIENTO_AUTO_MOTO
        break
    else:
        print(f'Dato {vehiculo} incorrecto, vuelva a intentarlo')

# Resultados
print('==================== Aulas ====================')
print(f'Aula asignada: {aula}')

print('========= Descuentos y Estacionamiento =========')
print(f'Turno: {turno.capitalize()}')
print(f'Materias: {materias}')
print(f'Valor de la cuota con descuento: ${cuota_con_descuento:.2f}')
print(f'Vehículo ingresado: {vehiculo.capitalize()}')
print(f'Costo del estacionamiento: ${costo_estacionamiento:.2f}')