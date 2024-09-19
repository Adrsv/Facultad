'''Crear un programa que permita registrar las inscripciones de los alumnos de una universidad
privada. Debe incluir un título principal, pedir los datos personales (nombre, edad, fecha de
nacimiento). Crear una variable que muestre True o False si posee título secundario (ese
dato no se pide al usuario, se escribe en el programa).
Además se deberá ingresar el monto de matrícula y calcular la cuota (valor de la matrícula +
$ 1000).
La materia "Python I" tiene un arancel especial, cuyo valor es $ 12000 por cuatrimestre.
Mostrar el costo mensual y calcular un descuento del 15% de la cuota para aquellos que
paguen en efectivo.
Finalmente se deberán imprimir todos los datos pedidos.'''

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
fecha = input("Ingrese su fecha de nacimiento: ")
titulo = True
matricula = int(input("Ingrese el monto de la matricula: "))

cuota_mensual= matricula + 1000

cuota= (4000 * 15) / 100
descuento= cuota + 4000

print('=========================')
print('Universidad de Python - Inscripciones')
print('=========================')
print('Datos de ingreso: ') 
print(f'nombre completo: {nombre}') 
print(f'Fecha de nacimiento: {fecha}')
print(f'Posee titulo? : {titulo}')
print(f'Matricula: {matricula}')
print(f'Cuota mensual: {cuota_mensual}')
print(f'Arancel mensual de la materia "Python 1": {4000}')
print(f'Arancel mensual de la materia "Python 1" con descuento: {descuento}')