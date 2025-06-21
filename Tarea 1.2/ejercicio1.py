import pandas as pd

# 1. Cargar los datos en un DataFrame
df = pd.read_csv('ventas.csv')

# Mostrar las primeras filas del DataFrame
print(" Primeras filas del DataFrame:")
print(df.head())

# 2. Calcular la cantidad total de productos vendidos por categoría
total_por_categoria = df.groupby('Producto')['Cantidad'].sum().reset_index()
print("\n Cantidad total de productos vendidos por categoría:")
print(total_por_categoria)

# 3. Determinar cuál es el producto con el mayor total de ventas
producto_ventas = df.groupby('Producto')['Cantidad'].sum()
producto_mayor_ventas = producto_ventas.idxmax()
print("\n Producto con mayor total de ventas:", producto_mayor_ventas)

# 4. Encontrar el precio promedio de los productos vendidos
precio_promedio = df['Precio_Unitario'].mean()
print("\n Precio promedio de los productos vendidos:", round(precio_promedio, 2))
