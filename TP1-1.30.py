# Primer caso - p(x) esta Normalizada

# Librerias
import numpy as np
import matplotlib.pyplot as plt

# p(x) - Normalizada
m1 = 0
s1 = 1

# Creamos la matriz que contendra los datos KL de la variación de los parametros
mz = 6    # Media size
sz = 6    # Variancia size

# Creamos los vector y las matrices de los parametros
mi = np.arange(0, mz)     # Vector de medias 
si = np.arange(1, sz)     # Vector de varianzas
mm, ss = np.meshgrid(mi,si) 
print('Medias: ',mm)
print('Varianzas: ',ss)

# Evaluamos los parametros en la definicion formal de KL
KL = np.log( np.sqrt(ss)/np.sqrt(s1) ) + (s1 + (m1-mm)**2 )/(2*ss) - 1/2
print(KL)
# Plot 
fig = plt.figure(dpi=100)

for i in range(0,sz-1):
  lbl = '$S^2 $= ' + str(i+1)
  plt.plot(mi, KL[i,:], label=lbl)

plt.xlabel(r'$m$')
plt.ylabel('KL Divergence values')
plt.title('$p(x)$ normalized  |  $\mu=0,  \sigma^2=1$')
plt.grid(True, linestyle='--')
plt.legend()


# Segundo caso - q(x) esta Normalizada
# q(x) - Normalizada
m2 = 0
s2 = 1

# Creamos la matriz que contendra los datos KL de la variación de los parametros
mz = 6    # Media size
sz = 6    # Variancia size

# Creamos los vector y las matrices de los parametros
mi = np.arange(0, mz)     # Vector de medias 
si = np.arange(1, sz)     # Vector de varianzas
mm, ss = np.meshgrid(mi,si) 
print('Medias: ',mm)
print('Varianzas: ',ss)

# Evaluamos los parametros en la definicion formal de KL
KL = np.log( np.sqrt(s2)/np.sqrt(ss) ) + (ss + (mm-m2)**2 )/(2*s2) - 1/2
print(KL)
# Plot 
fig = plt.figure(dpi=100)

for i in range(0,sz-1):
  lbl = '$\sigma^2 $= ' + str(i+1)
  plt.plot(mi, KL[i,:], label=lbl)

plt.xlabel(r'$\mu$')
plt.ylabel('KL Divergence values')
plt.title('$q(x)$ normalized  |  $m=0,  s^2=1$')
plt.grid(True, linestyle='--')
plt.legend()
