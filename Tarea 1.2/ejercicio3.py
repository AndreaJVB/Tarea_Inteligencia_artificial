import pandas as pd
#1. Cargue el dataset y muestre las primeras filas.
df = pd.read_csv('calificaciones.csv')
print(df)

#2. Calcule el promedio de calificaciones por materia.
promedio_calificaciones = df.groupby('Materia')['Calificación'].mean().reset_index()
print("\nPromedio de calificaciones por materia:")
print(promedio_calificaciones)

#3.  Identifique el estudiante con el promedio más alto.
estudiante_mejor_promedio = df.groupby('Estudiante')['Calificación'].mean().idxmax()
print("\nEstudiante con el promedio más alto:", estudiante_mejor_promedio)

#4. Agrupa las calificaciones por estudiante y calcule el promedio de cada uno.
promedio_estudiantes = df.groupby('Estudiante')['Calificación'].mean().reset_index()
print("\nPromedio de calificaciones por estudiante:")
print(promedio_estudiantes)

#5. Identifique cuántos estudiantes tienen un promedio superior a 85.
estudiantes_superior_85 = promedio_estudiantes[promedio_estudiantes['Calificación'] > 85]
cantidad_superior_85 = len(estudiantes_superior_85)
print("\nCantidad de estudiantes con promedio superior a 85:", cantidad_superior_85)

#6. Encuentre la materia con la mayor cantidad de calificaciones registradas.
materia_mayor_calificaciones = df['Materia'].value_counts().idxmax()
print("\nMateria con la mayor cantidad de calificaciones registradas:", materia_mayor_calificaciones)

#7. Muestre los 5 estudiantes con el promedio más bajo.
peor_promedio_estudiantes = promedio_estudiantes.sort_values(by='Calificación').head(5)

print("\nLos 5 estudiantes con el promedio más bajo:")
print(peor_promedio_estudiantes)

