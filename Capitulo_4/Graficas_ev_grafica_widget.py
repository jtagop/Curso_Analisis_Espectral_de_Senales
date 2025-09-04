import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

# Datos para la primera gráfica
def caja1(t):
    return np.where((t >= 0) & (t <= 1), 0.5, 0)

# Datos para la segunda gráfica
def caja2(t, desp):
    return np.where((t >= 0+desp) & (t <= 1+desp), 1, 0)

def grafica_interactiva(desp):
    # Crear la gráfica
    fig, ax = plt.subplots(figsize=(6, 6))
    # Configuración de gráfica
    t = np.linspace(-3, 3, 1000)
    ax.plot(t, caja1(t), label='e(τ)', color='blue')
    ax.plot(t, caja2(t, desp), label='e(t-τ)', color='red')
    ax.set_title('Función de transferencia', fontsize=12, fontweight='bold')
    ax.set_xlabel('τ', fontsize=12, fontweight='bold')
    ax.set_ylabel('h(τ)', fontsize=12, fontweight='bold')
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 1.5)
    ax.set_xticks(np.arange(-2, 3)) 
    ax.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
    ax.text(3, -0.1, '$+\infty$', ha='center', va='bottom')
    plt.legend()
    plt.show()

# Crear widget deslizante para modificar p1
widget = widgets.FloatSlider(
    value=0,
    min=-2,
    max=2,
    step=0.01,
    description='Valor de desp:',
    continuous_update=True
)

# Vincular el widget con la función actualizar_grafica
widgets.interactive(grafica_interactiva, desp=widget)