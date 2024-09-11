import matplotlib.pyplot as plt

# Coordenadas de los puntos que forman los triángulos abiertos
x1 = [10, 20, 30]  # Vértices en el eje X del primer triángulo
y1 = [20, 40, 10]  # Vértices en el eje Y del primer triángulo
x2 = [10, 20, 30]  # Vértices en el eje X del segundo triángulo
y2 = [40, 10, 30]  # Vértices en el eje Y del segundo triángulo

# Crear el gráfico con diferentes colores
plt.plot(x1, y1, marker='o', linestyle='-', color='r', label='Triángulo 1 (Rojo)')  # Color rojo para el primer triángulo
plt.plot(x2, y2, marker='o', linestyle='-', color='g', label='Triángulo 2 (Verde)')  # Color verde para el segundo triángulo

# Títulos y etiquetas
plt.title('Gráfico con dos triángulos abiertos de diferentes colores')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

# Mostrar leyenda
plt.legend()

# Mostrar el gráfico
plt.show()
