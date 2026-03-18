if promedio >= 4.5 and reprobadas == 0:
    clasificacion = "Excelente"

elif promedio >= 3.8 and reprobadas <= 1:
    clasificacion = "Bueno"

elif promedio >= 3.0:
    clasificacion = "En riesgo"

else:
    clasificacion = "Crítico"
