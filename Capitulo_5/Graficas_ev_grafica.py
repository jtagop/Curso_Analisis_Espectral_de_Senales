import numpy as np
import matplotlib.pyplot as plt

def x(t):
    return np.where((t>=0) & (t<=1),1,0)
def h(t):
    return np.where((t>=0) & (t<=1),t,0)

#variables

desplazamiento1 = 1
desplazamiento2 = -1
t = np.linspace(-2.000001,3.000001,100)

# Primer paso
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# e(t)
ax1.plot(t,x(t),color='blue')
ax1.set_title('Función de entrada', fontsize=12, fontweight='bold')
ax1.set_xlabel('t', fontsize=12, fontweight='bold')
ax1.set_ylabel('x(t)', fontsize=12, fontweight='bold')
ax1.set_xlim(-3,3)
ax1.set_ylim(0, 1.5)
ax1.set_xticks(np.arange(-2,3)) 
ax1.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
ax1.text(3, -0.1, '$+\infty$', ha='center', va='bottom')

# h(t)
ax2.plot(t,h(t),color='red')
ax2.set_title('Función de transferencia', fontsize=12, fontweight='bold')
ax2.set_xlabel('t', fontsize=12, fontweight='bold')
ax2.set_ylabel('h(t)', fontsize=12, fontweight='bold')
ax2.set_xlim(-3,3)
ax2.set_ylim(0, 1.5)
ax2.set_xticks(np.arange(-2,3)) 
ax2.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
ax2.text(3, -0.1, '$+\infty$', ha='center', va='bottom')

# Mostramos la gráfica
plt.tight_layout()
plt.show()

#Paso 2
# Primer paso
fig, (ax2) = plt.subplots(figsize=(6, 6))

# h(t)
ax2.plot(t,h(t),color='red')
ax2.set_title('Función de transferencia', fontsize=12, fontweight='bold')
ax2.set_xlabel('τ', fontsize=12, fontweight='bold')
ax2.set_ylabel('h(τ)', fontsize=12, fontweight='bold')
ax2.set_xlim(-3,3)
ax2.set_ylim(0, 1.5)
ax2.set_xticks(np.arange(-2,3)) 
ax2.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
ax2.text(3, -0.1, '$+\infty$', ha='center', va='bottom')

# Mostramos la gráfica
plt.tight_layout()
plt.show()

#Paso 3.1
# Primer paso
fig, (ax2) = plt.subplots(figsize=(6, 6))

# h(t)
ax2.plot(t,h(t-1),color='red')
ax2.set_title('Función de transferencia', fontsize=12, fontweight='bold')
ax2.set_xlabel('τ', fontsize=12, fontweight='bold')
ax2.set_ylabel('h(τ)', fontsize=12, fontweight='bold')
ax2.set_xlim(-3,3)
ax2.set_ylim(0, 1.5)
ax2.set_xticks(np.arange(-2,3)) 
ax2.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
ax2.text(3, -0.1, '$+\infty$', ha='center', va='bottom')

# Agregar línea para indicar el desplazamiento
ax2.plot([0, desplazamiento1], [0.05, 0.05], color='black', linestyle='--', label=f't: {desplazamiento1}')
# Mostrar leyenda
ax2.legend()
# Mostramos la gráfica
plt.tight_layout()
plt.show()

#Paso 3.2
# Primer paso
fig, (ax2) = plt.subplots(figsize=(6, 6))

# h(t)
ax2.plot(t,h(t+1),color='red')
ax2.set_title('Función de transferencia', fontsize=12, fontweight='bold')
ax2.set_xlabel('τ', fontsize=12, fontweight='bold')
ax2.set_ylabel('h(τ)', fontsize=12, fontweight='bold')
ax2.set_xlim(-3,3)
ax2.set_ylim(0, 1.5)
ax2.set_xticks(np.arange(-2,3)) 
ax2.text(-3, -0.1, '$-\infty$', ha='center', va='bottom')
ax2.text(3, -0.1, '$+\infty$', ha='center', va='bottom')

# Agregar línea para indicar el desplazamiento
ax2.plot([0, desplazamiento2], [0.05, 0.05], color='black', linestyle='--', label=f't: {desplazamiento1}')
# Mostrar leyenda
ax2.legend()
# Mostramos la gráfica
plt.tight_layout()
plt.show()