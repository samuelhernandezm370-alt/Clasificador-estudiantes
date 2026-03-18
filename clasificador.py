promedio = float(input("Ingrese el promedio académico: "))
materias_reprobadas = int(input("Ingrese la cantidad de materias reprobadas: "))
horas_estudio = float(input("Horas de estudio por día: "))
asistencia = input("Nivel de asistencia (alta, media, baja): ")

print("\n--- Analizando desempeño académico ---\n")

if promedio >= 4.5 and materias_reprobadas == 0:
    clasificacion = "Excelente"

elif promedio >= 3.8 and materias_reprobadas <= 1:
    clasificacion = "Bueno"

elif promedio >= 3.0:
    clasificacion = "En riesgo"

else:
    clasificacion = "Crítico"


print("Clasificación académica:", clasificacion)


if horas_estudio >= 4:
    print("Buen hábito de estudio")

elif horas_estudio >= 2:
    print("Hábito de estudio aceptable")

else:
    print("Debe mejorar sus hábitos de estudio")


if asistencia == "alta":
    print("Excelente asistencia")

elif asistencia == "media":
    print("Asistencia regular")

else:
    print("Baja asistencia, se recomienda mejorarla")