import matplotlib.pyplot as plt

# Coordenadas de los puntos que forman el triángulo abierto
x = [1, 4, 5, 6, 7]  # Vértices en el eje X
y = [2, 6, 3, 6, 3]  # Vértices en el eje Y

# Crear el gráfico con línea de puntos suspensivos
plt.plot(x, y, marker='o', linestyle=':', color='b', label='Puntos suspensivos')

# Títulos y etiquetas
plt.title('Gráfico con puntos suspensivos')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
