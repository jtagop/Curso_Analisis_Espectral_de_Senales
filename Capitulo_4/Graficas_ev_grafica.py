import numpy as np
import matplotlib.pyplot as plt

# Datos para la primera gráfica
def caja1(t):
    return np.where((t >= 0) & (t <= 1), 0.5, 0)

# Datos para la segunda gráfica
def caja2(t):
    return np.where((t >= 0) & (t <= 1), 1, 0)
# Datos para la tercer gráfica
def caja2_1(t):
    return np.where((t >= -1) & (t <= 0), 1, 0)
# Datos para la gráfica desplazada
def caja2_desp(t,desplazamiento):
    return np.where((t >= -1+desplazamiento) & (t <= 0+desplazamiento), 1, 0)

desplazamiento = 0.25
t = np.linspace(-0.000001,1.000001,100)
t_1 = np.linspace(-1.000001,0.000001,100)
t_desp = np.linspace(-1.000001+desplazamiento,0.000001+desplazamiento,100)

# Primer paso
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# e(t)
ax1.plot(t,caja1(t),color='blue')
ax1.set_title('Función de entrada', fontsize=12, fontweight='bold')
ax1.set_xlabel('t', fontsize=12, fontweight='bold')
ax1.set_ylabel('e(t)', fontsize=12, fontweight='bold')
ax1.set_xlim(-5,5)
ax1.set_ylim(0, 1.5)
ax1.set_xticks(np.arange(-4,5)) 
ax1.text(-5, -0.1, '$-\infty$', ha='center', va='bottom')
ax1.text(5, -0.1, '$+\infty$', ha='center', va='bottom')

# h(t)
ax2.plot(t,caja2(t),color='red')
ax2.set_title('Función de transferencia', fontsize=12, fontweight='bold')
ax2.set_xlabel('t', fontsize=12, fontweight='bold')
ax2.set_ylabel('h(t)', fontsize=12, fontweight='bold')
ax2.set_xlim(-5,5)
ax2.set_ylim(0, 1.5)
ax2.set_xticks(np.arange(-4,5)) 
ax2.text(-5, -0.1, '$-\infty$', ha='center', va='bottom')
ax2.text(5, -0.1, '$+\infty$', ha='center', va='bottom')

# Mostramos la gráfica
plt.tight_layout()
plt.show()

# Paso 2
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# e(tau)
ax1.plot(t,caja1(t),color='blue')
ax1.set_title('Función de entrada', fontsize=12, fontweight='bold')
ax1.set_xlabel('τ', fontsize=12, fontweight='bold')
ax1.set_ylabel('e(τ)', fontsize=12, fontweight='bold')
ax1.set_xlim(-5,5)
ax1.set_ylim(0, 1.5)
ax1.set_xticks(np.arange(-4,5)) 
ax1.text(-5, -0.1, '$-\infty$', ha='center', va='bottom')
ax1.text(5, -0.1, '$+\infty$', ha='center', va='bottom')

# h(tau)
ax2.plot(t,caja2(t),color='red')
ax2.set_title('Función de transferencia', fontsize=12, fontweight='bold')
ax2.set_xlabel('τ', fontsize=12, fontweight='bold')
ax2.set_ylabel('h(τ)', fontsize=12, fontweight='bold')
ax2.set_xlim(-5,5)
ax2.set_ylim(0, 1.5)
ax2.set_xticks(np.arange(-4,5)) 
ax2.text(-5, -0.1, '$-\infty$', ha='center', va='bottom')
ax2.text(5, -0.1, '$+\infty$', ha='center', va='bottom')

# Mostramos la gráfica
plt.tight_layout()
plt.show()

# Paso 3
fig, ax = plt.subplots(figsize=(6, 6))

# h(-tau)
ax.plot(t_1,caja2_1(t_1),color='red')
ax.set_title('Función de transferencia', fontsize=12, fontweight='bold')
ax.set_xlabel('τ', fontsize=12, fontweight='bold')
ax.set_ylabel('h(τ)', fontsize=12, fontweight='bold')
ax.set_xlim(-3,3)
ax.set_ylim(0, 1.5)
ax.set_xticks(np.arange(-2,3)) 
ax.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
ax.text(3, -0.1, '$+\infty$', ha='center', va='bottom')

# Mostramos la gráfica
plt.show()

# Paso 4
fig, ax = plt.subplots(figsize=(6, 6))

# h(t-tau)
ax.plot(t_desp,caja2_desp(t_desp,desplazamiento),color='red')
ax.set_title('Función de transferencia', fontsize=12, fontweight='bold')
ax.set_xlabel('τ', fontsize=12, fontweight='bold')
ax.set_ylabel('h(τ)', fontsize=12, fontweight='bold')
ax.set_xlim(-3,3)
ax.set_ylim(0, 1.5)
ax.set_xticks(np.arange(-2,3)) 
ax.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
ax.text(3, -0.1, '$+\infty$', ha='center', va='bottom')

# Agregar línea para indicar el desplazamiento
ax.plot([0, desplazamiento], [0, 0], color='black', linestyle='--', label=f't: {desplazamiento}')
# Mostrar leyenda
ax.legend()
# Mostramos la gráfica
plt.show()

# Paso 1 analitico
fig, ax = plt.subplots(figsize=(12, 6))

# h(t-tau)
ax.plot(t_desp,caja2_desp(t_desp,desplazamiento),color='red', label = 'h(t-τ)')
ax.plot(t,caja1(t),color='blue', label = 'e(τ)')
ax.set_title('Función de transferencia', fontsize=12, fontweight='bold')
ax.set_xlabel('τ', fontsize=12, fontweight='bold')
ax.set_ylabel('s(t)', fontsize=12, fontweight='bold')
ax.set_xlim(-3,3)
ax.set_ylim(0, 1.5)
ax.set_xticks(np.arange(-2,3)) 
ax.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
ax.text(3, -0.1, '$+\infty$', ha='center', va='bottom')

# Agregar línea para indicar el desplazamiento
ax.plot([0, desplazamiento], [0, 0], color='black', linestyle='--', label=f't: {desplazamiento}')
# Mostrar leyenda
ax.legend()
# Mostramos la gráfica
plt.show()