import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# Datos para la primera gráfica
def caja1(t):
    return np.where((t >= 0) & (t <= 1), 0.5, 0)

# Datos para la segunda gráfica
def caja2(t, desp):
    return np.where((t >= -1+desp) & (t <= 0+desp), 1, 0)

# Función de convolución
def calcular_s(t, desp):
    if t < 0 or t > 2:
        return 0
    elif 0 <= t <= 1:
        return 0.5 * desp
    else:
        return 0.5 * (2 - desp)

t = np.linspace(-3, 3, 100)

# Crear figura y ejes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plotear las gráficas
line1, = ax1.plot(t, caja1(t), label='e(τ)', color='blue')
line2, = ax1.plot(t, caja2(t, 0), label='e(t-τ)', color='red')

# Función para actualizar la gráfica
def animate(i):
    ax1.cla()  # Limpiar el eje
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(0, 1.5)
    ax1.text(-3, -0.1, '$-\infty$', ha='center', va='bottom', fontsize=12)
    ax1.text(3, -0.1, '$+\infty$', ha='center', va='bottom', fontsize=12)
    ax1.plot(t, caja1(t), label='e(τ)', color='blue')
    ax1.plot(t, caja2(t, i/2), label='e(t-τ)', color='red')
    mascara = (t >= -1+i/2) & (t <= 0+i/2) & (t >= 0) & (t <= 1)
    ax1.fill_between(t, caja1(t), where=mascara, color='green', alpha=0.5)
    ax1.set_xlabel('t', fontsize=12, fontweight='bold')
    ax1.set_ylabel('s(t)', fontsize=12, fontweight='bold')
    ax1.legend()

    # Actualizar gráfica de convolución
    ax2.cla()  # Limpiar el eje
    ax2.set_title('Convolución', fontsize=12, fontweight='bold')
    ax2.set_xlabel('t', fontsize=12, fontweight='bold')
    ax2.set_ylabel('s(t)', fontsize=12, fontweight='bold')
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(0, 1)
    ax2.set_xticks(np.arange(-2, 3)) 
    ax2.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
    ax2.text(3, -0.1, '$+\infty$', ha='center', va='bottom')

    t_s = np.linspace(-3, 3, 1000)
    idx = int((i/2 + 3) / 6 * len(t_s))  # Índice para slicing
    s_values = [calcular_s(ti,ti) for ti in t_s[:idx]]  # Valores de s hasta idx
    ax2.plot(t_s[:idx], s_values, label='s(t)', color='purple')  # Gráfica hasta idx
    ax2.legend()

    return

# Crear animación
ani = animation.FuncAnimation(fig, animate, frames=20, interval=500, repeat=True, repeat_delay=100)

# Guardar la animación como GIF
ani.save('ani_intconv.gif', fps=2)

# Mostrar gráfica
plt.show()