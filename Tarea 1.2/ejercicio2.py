import pandas as pd

# 1. Cargar el dataset y convertirlo en un DataFrame
df = pd.read_csv('clima.csv')

# 2. Calcular la temperatura promedio de cada ciudad
temperatura_promedio = df.groupby('Ciudad')['Temperatura'].mean()
print("\nTemperatura promedio por ciudad:")
print(temperatura_promedio)

# 3. Determinar el registro con la temperatura más alta y más baja en el dataset
registro_max = df.loc[df['Temperatura'].idxmax()]
registro_min = df.loc[df['Temperatura'].idxmin()]
print("\nRegistro con la temperatura más alta:")
print(registro_max)
print("\nRegistro con la temperatura más baja:")
print(registro_min)

# 4. Identificar qué ciudad tuvo la temperatura más alta y cuál la más baja
ciudad_max = registro_max['Ciudad']
ciudad_min = registro_min['Ciudad']
print("\nCiudad con la temperatura más alta:", ciudad_max)
print("Ciudad con la temperatura más baja:", ciudad_min)

# 5. Encontrar cuántos registros tienen temperatura mayor a 30°C
registros_mayor_30 = df[df['Temperatura'] > 30]
cantidad_mayor_30 = len(registros_mayor_30)
print("\nCantidad de registros con temperatura mayor a 30°C:", cantidad_mayor_30)

# 6. Contar cuántos días hay registrados por cada ciudad
conteo_ciudades = df['Ciudad'].value_counts()
print("\nCantidad de días registrados por ciudad:")
print(conteo_ciudades)
