import matplotlib.pyplot as plt

def graficar():
    # Datos a graficar
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    # Crear la gráfica de línea
    plt.plot(x, y, label='Línea de Ejemplo')

    # Añadir etiquetas y título
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Gráfico de Línea')

    # Añadir leyenda
    plt.legend()

    # Guardar la gráfica como una imagen PNG
    plt.savefig('grafico.png')

# Llamar a la función para graficar
graficar()
