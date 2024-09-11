import matplotlib.pyplot as plt

# Coordenadas de los puntos que forman el triángulo abierto
x = [1, 2, 3]  # Vértices en el eje X
y = [2, 4, 1]  # Vértices en el eje Y

# Crear el gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b', label='Triángulo abierto')

# Títulos y etiquetas
plt.title('Gráfico de triángulo abierto desde 1.0 a 3.0')
plt.xlabel(' X')
plt.ylabel(' Y')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
