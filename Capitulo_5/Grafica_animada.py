import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# Funciones
def x(t):
    return np.where((t >= 0) & (t <= 1), 1, 0)

def h_corr(t, desp):
    return np.where((t >= -desp) & (t <= 1 - desp), t + desp, 0)

def correlacion_valor(t_val):
    t_int = np.linspace(-1, 2, 1000)
    integrando = x(t_int) * h_corr(t_int, t_val)
    return np.trapz(integrando, t_int)

# Rango temporal para la correlación
t_vals = np.linspace(-1, 2, 100)
r_vals = np.array([correlacion_valor(tv) for tv in t_vals])

# Tiempo para el eje τ
t_tau = np.linspace(-3, 3, 1000)

# Crear figura
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

def animate(i):
    ax1.cla()
    t_shift = t_vals[i]
    h_t = h_corr(t_tau, t_shift)
    
    ax1.plot(t_tau, x(t_tau), label='e(τ)', color='blue')
    ax1.plot(t_tau, h_t, label='h(t+τ)', color='red')
    ax1.fill_between(t_tau, x(t_tau) * h_t, color='green', alpha=0.5)
    ax1.set_xlim(-1, 2)
    ax1.set_ylim(0, 1.5)
    ax1.set_xlabel('τ')
    ax1.set_title(f't = {t_shift:.2f}')
    ax1.legend()

    ax2.cla()
    ax2.plot(t_vals[:i+1], r_vals[:i+1], label='r(t)', color='purple')
    ax2.set_xlim(-1, 2)
    ax2.set_ylim(0, max(r_vals) + 0.1)
    ax2.set_xlabel('t')
    ax2.set_title('Correlación cruzada $R_{xh}(t)$')
    ax2.legend()

# Crear animación
ani = animation.FuncAnimation(fig, animate, frames=len(t_vals), interval=150, repeat=True, repeat_delay=1000)

# Guardar GIF
ani.save('correlacion_acumulada.gif', fps=10)

# Mostrar
plt.show()

