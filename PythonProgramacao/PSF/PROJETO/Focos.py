import json
import matplotlib.pyplot as plt
import numpy as np

# Entrada dos parâmetros
entrada = json.loads('{"vp":1022, "G":6.67430e-11, "M":5.97219e24, "m":7.34767309e22, "dt":10, "x0":-384400000, "y0":0}')

vp = entrada['vp']
G = entrada['G']
M = entrada['M']
m = entrada['m']
dt = entrada['dt']
x = entrada['x0']
y = entrada['y0']
t = 0
vx = 0
vy = vp
xt = 0
yt = 0

x_lista = []
y_lista = []
#plt.gca().set_aspect('equal')

# Variáveis para armazenar os pontos de apogeu e perigeu
distancia_max = 0
distancia_min = float('inf')

# Definindo loop
while t < 54 * 3600 * 24:
#   Calculando posição da Terra
    r = ((x - xt) ** 2 + (y - yt) ** 2) ** 0.5

#   Atualizando a distância máxima e mínima
    if r > distancia_max:
        distancia_max = r
    if r < distancia_min:
        distancia_min = r

#   Calculando a aceleração
    a = (-G * M) / (r ** 3)
    ax = a * (x - xt)
    ay = a * (y - yt)

#   Atualizando velocidades
    vx += ax * dt
    vy += ay * dt

#   Atualizando posições
    yanterior = y
    x += vx * dt
    y += vy * dt

    if (yanterior < 0) and (y > 0):
        tempo = t / 3600 / 24
        print(f"Tempo órbita: {tempo:.4f}")

    x_lista.append(x)
    y_lista.append(y)

#   Atualizando tempo
    t += dt

# Calculando semi-eixo maior (a), semi-eixo menor (b) e excentricidade (e)
a = (distancia_max + distancia_min) / 2
b = np.sqrt(distancia_max * distancia_min)
e = np.sqrt(1 - (b ** 2 / a ** 2))
c = a * e

# Coordenadas dos focos
foco1 = (-c, 0)
foco2 = (c, 0)

# Exibindo os focos
print(f"Os focos da elipse são: {foco1} e {foco2}")

# Plotando a órbita
plt.gca().set_aspect('equal')
plt.plot(x_lista, y_lista)
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Órbita da Lua em torno da Terra')
plt.grid()
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.scatter([foco1[0], foco2[0]], [foco1[1], foco2[1]], color='red', marker='x', label='Focos')
plt.legend()
plt.savefig('Focos.pdf')
plt.close('all')
