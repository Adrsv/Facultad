def Ejercicio():

    numeros = []
    
    for i in range(1, 4):
        num = int(input('Ingrese un numero: '))
        numeros.append(num)  # Se añade el número ingresado a la lista
    
    # Ordenar la lista de números en orden descendente (de mayor a menor)
    numeros.sort(reverse=True)
    
    # Condicional que verifica si el mayor número es mayor que el segundo
    if numeros[0] > numeros[1]:
        print(f'El numero {numeros[0]} es el mayor')
    else:
        print('No existe')
    
    print(numeros)


Ejercicio()