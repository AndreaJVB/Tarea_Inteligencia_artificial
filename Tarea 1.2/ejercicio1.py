import pandas as pd

##cargar los datos en un DataFrame
df = pd.read_csv('ventas.csv')

print(df)
##Calcule la cantidad total de productos vendidos por categoria
total_por_categoria = df.groupby('Producto')['Cantidad'].sum().reset_index()

##Determine cual es el producto con el mayor total de ventas
producto_mayor_ventas = df.groupby('Producto')['Cantidad'].sum().idxmax()

##Encuentre el precio promedio de los productos vendidos
preco_promedio = df['Precio_Unitario'].mean()

print("DataFrame: ", df)
print("Total por categoria:\n", total_por_categoria)
print("Producto con mayor total de ventas:", producto_mayor_ventas)
print("Precio promedio de los productos vendidos:", preco_promedio)