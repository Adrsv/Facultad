def calcular_vuelto(total_compra, dinero_recibido):
    # Verificar si el dinero recibido es suficiente
    if dinero_recibido < total_compra:
        return "Error: el dinero recibido es insuficiente."
    
    # Cálculo del vuelto
    vuelto = dinero_recibido - total_compra
    
    # Denominaciones de billetes
    denominaciones = [500, 100, 50, 20, 10, 5, 1]
    
    # Diccionario para almacenar cuántos billetes de cada denominación se necesitan
    billetes = {}
    
    # Calcular la cantidad de billetes para cada denominación
    for billete in denominaciones:
        cantidad_billetes = vuelto // billete
        if cantidad_billetes > 0:
            billetes[billete] = cantidad_billetes
        vuelto %= billete
    
    # Formatear el resultado
    resultado = "Billetes entregados:\n"
    for billete, cantidad in billetes.items():
        resultado += f"{cantidad} billete(s) de ${billete}\n"
    
    return resultado

# Input del usuario
total_compra = int(input("Ingrese el total de la compra: "))
dinero_recibido = int(input("Ingrese el dinero recibido: "))

# Llamar a la función y mostrar el resultado
print(calcular_vuelto(total_compra, dinero_recibido))
