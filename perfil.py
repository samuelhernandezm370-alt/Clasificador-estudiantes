# Perfil del estudiante

if interes.lower() == "programacion" and horas_estudio >= 3:
    perfil = "Perfil técnico"

elif interes.lower() == "matematicas" or interes.lower() == "analisis de datos":
    perfil = "Perfil analítico"

elif asistencia.lower() == "alta" and horas_estudio >= 2:
    perfil = "Perfil disciplinado"

else:
    perfil = "Perfil por fortalecer"


# Recomendación Academica

if clasificacion == "En riesgo" and materias_reprobadas >= 2:
    recomendacion = "Asistir a tutorías y reforzar materias reprobadas"

elif clasificacion == "En riesgo":
    recomendacion = "Asistir a tutorías académicas"

elif clasificacion == "Crítico":
    recomendacion = "Solicitar acompañamiento académico urgente"

elif horas_estudio < 2:
    recomendacion = "Reforzar hábitos de estudio (mínimo 2 horas diarias)"

elif asistencia.lower() == "baja":
    recomendacion = "Mejorar la asistencia a clases"

elif interes.lower() == "programacion":
    recomendacion = "Participar en proyectos de programación"

else:
    recomendacion = "Explorar actividades académicas adicionales"