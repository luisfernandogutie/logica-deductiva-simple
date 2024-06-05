from pyDatalog import pyDatalog

# Crear términos
pyDatalog.create_terms('X, estudiante, promedio_alto, faltas_pocas, actividad_extracurricular')

# Definir hechos
+ promedio_alto('Juan')
+ faltas_pocas('Juan')
+ actividad_extracurricular('Juan')

+ promedio_alto('María')
+ faltas_pocas('María')

+ promedio_alto('Pedro')
+ actividad_extracurricular('Pedro')


# Definir reglas
def elegible(estudiante):
    return promedio_alto(estudiante) & faltas_pocas(estudiante) & actividad_extracurricular(estudiante)