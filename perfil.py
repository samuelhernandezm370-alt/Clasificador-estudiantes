if intereses == "tecnologia" and horas_estudio >= 3:
    perfil = "Perfil técnico"

elif intereses == "ciencias" and horas_estudio >= 3:
    perfil = "Perfil científico"

elif intereses == "arte":
    perfil = "Perfil creativo"

elif intereses == "deportes":
    perfil = "Perfil deportivo"

elif intereses == "emprendimiento":
    perfil = "Perfil emprendedor"

elif asistencia == "alta" and horas_estudio >= 2:
    perfil = "Perfil disciplinado"

elif asistencia == "baja" and horas_estudio < 2:
    perfil = "Perfil desmotivado"

elif horas_estudio >= 4:
    perfil = "Perfil altamente dedicado"

else:
    perfil = "Perfil por fortalecer"



if clasificacion == "En riesgo" and materias_reprobadas >= 2:
    recomendacion = "Asistir a tutorías y reforzar materias reprobadas"

elif clasificacion == "En riesgo":
    recomendacion = "Asistir a tutorías académicas"

elif clasificacion == "Crítico":
    recomendacion = "Solicitar acompañamiento académico urgente"

elif horas_estudio < 2:
    recomendacion = "Reforzar hábitos de estudio (mínimo 2 horas diarias)"

elif asistencia == "baja":
    recomendacion = "Mejorar la asistencia a clases"

elif intereses == "tecnologia":
    recomendacion = "Participar en proyectos tecnológicos"

else:
    recomendacion = "Explorar actividades académicas adicionales"
