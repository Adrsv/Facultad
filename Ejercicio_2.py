'''La universidad ahora pide un programa que permita cargar las notas de dos exámenes y
obtener el promedio. Además deberá determinar si el alumno aprobó el último examen
(nota mayor o igual a 7), en caso contrario informar que desaprobó.
Además se desea saber si el alumno mejoró, empeoró o mantuvo su desempeño entre
ambos parciales. Para ello se deberá informar "Mejoró su desempeño" si la nota del
segundo parcial es mayor que la del primero, "Mantuvo la nota" si ambas notas son
iguales o "Empeoró su desempeño" si la nota del primer parcial es mayor que la del
segundo.
Finalmente, la universidad desea saber si el alumno promocionó la materia (promedio
mayor o igual a 7), debe rendir final (promedio mayor o igual a 4) o debe recursar'''

notas= []
i= 1

while True:
    nota= float(input(f'Ingrese la nota del examen {i}, ingrese 0 para finalizar: '))
    if nota == 0:
        break
    if nota <= 10 and nota > 0:
        i= i + 1
        notas.append(nota)
    else:
        print(f'Nota {nota} incorrecta, vuelva a intentarlo')
if len(notas) == 2:
    if notas[0] == notas[1]:
        print('El alumno mantuvo la nota')
    elif notas[1] > notas[0]:
        print('El alumno mejoró su desempeño')
    else:
        print('El alumno empeoró su desempeño')

promedio= sum(notas) / len(notas)

if promedio >= 7:
    print(f'El alumno promocionó la materia con {promedio}')
elif promedio >= 4:
    print(f'El alumno debe rendir final con {promedio}')
else:
    print('Debe rendir final')

print(f'El alumno tuvo un promedio de {promedio}')