import pandas as pd
import matplotlib.pyplot as plt

# Carga de datos
data = pd.read_csv('ventas.csv')

# Cálculo de totales y estadísticas
total_ventas = data['Venta'].sum()
promedio_ventas = data['Venta'].mean()
venta_max = data['Venta'].max()
venta_min = data['Venta'].min()
dia_venta_max = data.loc[data['Venta'].idxmax(), 'Fecha']
dia_venta_min = data.loc[data['Venta'].idxmin(), 'Fecha']

# Mostrando los resultados calculados
print(f"Total de ventas: {total_ventas}")
print(f"Promedio de ventas diarias: {promedio_ventas:.2f}")
print(f"Venta máxima: {venta_max} el {dia_venta_max}")
print(f"Venta mínima: {venta_min} el {dia_venta_min}")

# Visualización de las ventas diarias
plt.figure(figsize=(10, 5))
plt.plot(data['Fecha'], data['Venta'], marker='o', linestyle='-', color='b')
plt.title('Ventas Diarias en Enero 2023')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()  # Ajusta automáticamente los parámetros de la figura para dar espacio a los labels
plt.show()
