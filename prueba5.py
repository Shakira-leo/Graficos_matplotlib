import matplotlib.pyplot as plt
import numpy as np

# Crear datos
x = np.linspace(0, 5, 20)  # 20 puntos entre 0 y 5
y1 = x ** 2  # y1 es x al cuadrado
y2 = x ** 3  # y2 es x al cubo
y3 = x ** 0.0  # y3 es x elevado a 1.5 para que esté debajo de los cuadrados

# Crear el gráfico
plt.figure(figsize=(8, 6))  # Configuración del tamaño de la figura

# Dibujar las tres líneas con diferentes marcadores y colores
plt.plot(x, y1, 's', color='b', label='Cuadrados (Azul)')  # Primera curva en azul con marcadores cuadrados
plt.plot(x, y2, '^', color='brown', label='Cubos (Marrón)')  # Segunda curva en marrón con marcadores triangulares
plt.plot(x, y3, linestyle='--', color='g', label='Potencia 1.5 (Verde)')  # Tercera curva en verde con línea discontinua (guiones)

# Etiquetas y leyenda
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.legend()

# Mostrar el gráfico
plt.show()
