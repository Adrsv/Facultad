# Listado de aulas

def listado_aulas():
    Aulas = {
        1: 'A-315',
        2: 'A-300',
        3: 'A-315',
        4: 'A-300',
        5: 'A-315',
        6: 'A-300',
    }

    salida = []  # Lista para almacenar el resultado formateado

    salida.append(f"Dia Aula")  # Encabezado de la tabla

    # Recorre el diccionario de aulas y agrega el formato "día aula" a la lista
    for key, value in Aulas.items():
        salida.append(f"{key} {value}")

    # Imprime cada línea de la lista de salida
    for linea in salida:
        print(linea)

def carga_edades():
    errores = 0  # Contador de errores

    print('========= Carga de edades =========')
    
    # Bucle infinito hasta que se ingrese una edad válida
    while True:
        edad = int(input('Ingrese una edad mayor o igual a 18: '))
        
        # Verificación de que la edad sea válida
        if edad < 18:
            print(f'Edad {edad} invalida, vuelva a intentarlo')
            errores += 1 
        else:
            print(f'La edad ingresada es: {edad}')
            print(f'Se ha ingresado la edad erroneamente {errores} veces')
            break  # Sale del bucle al ingresar una edad válida

def promedios():
    suma = 0  # suma de las notas

    print('========= Promedio de notas =========')
    
    # Recorre un ciclo para pedir 5 notas
    for i in range(1, 6):
        while True:
            nota = float(input(f'Ingrese la nota del alumno {i}: '))
            # Verifica que la nota sea válida (entre 0 y 10)
            if nota > 10 or nota < 0:
                print(f'La nota {nota} es invalida, vuelva a intentarlo')
            else:
                break
        
        suma += nota  # Acumula la nota ingresada
        promedio = suma / i  # Calcula el promedio parcial
    
    # Imprime el promedio final formateado a 2 decimales
    print(f'El promedio de notas es: {promedio:.2f}')

def comedor():
    print('========= Costo del comedor =========')
    
    costo = 1250  # Costo diario del comedor
    
    print('Dia  Costo')
    
    # Calcula y muestra el costo acumulado por día (de 1 a 6)
    for i in range(1, 7):
        total_costo = costo * i  # Calcula el costo total acumulado
        print(i, '  $', total_costo)  # Imprime el día y el costo correspondiente

# Llamada a las funciones
listado_aulas()
carga_edades()
promedios()
comedor()