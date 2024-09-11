import matplotlib.pyplot as plt

# Coordenadas de los puntos que forman el triángulo abierto
x = [3.0, 4.0, 3.0]  # Vértices en el eje X
y = [2.0, 3.0, 2.0]  # Vértices en el eje Y

# Crear el gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Triángulo abierto')

# Títulos y etiquetas
plt.title('Gráfico de triángulo abierto desde 1.0 a 3.0')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
