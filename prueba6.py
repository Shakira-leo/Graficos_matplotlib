import matplotlib.pyplot as plt
import numpy as np

# Datos del gráfico (puedes ajustarlos según sea necesario)
fechas = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']
valores = [772.5, 776.5, 776.6, 777.0, 775.0]

# Convertir las fechas en números para usarlas en el gráfico
x = np.arange(len(fechas))

# Crear el gráfico
plt.plot(x, valores, marker='o', linestyle='-', color='red')

# Añadir etiquetas a los puntos
for i, v in enumerate(valores):
    plt.text(i, v, f'{v}', ha='right', va='bottom')

# Añadir títulos y etiquetas a los ejes
plt.title('Gráfico de Valores por Fecha')
plt.xlabel('Fecha')
plt.ylabel('Valor')

# Mostrar el gráfico
plt.show()
