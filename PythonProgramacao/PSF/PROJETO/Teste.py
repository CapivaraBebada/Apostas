import json
import tkinter as tk
import numpy as np

# Parâmetros fornecidos
parametros = '{"vp":1022, "G":6.67430e-11, "M":5.97219e24, "m":7.34767309e22, "dt":10000, "x0":-384400000, "y0":0}'

# Entrada dos parâmetros
entrada = json.loads(parametros)

vp = entrada['vp']
G = entrada['G']
M = entrada['M']
m = entrada['m']
dt = entrada['dt']
x = entrada['x0']
y = entrada['y0']
vx = 0
vy = vp
xt = 0
yt = 0
x_lista = []
y_lista = []
t = 0

# Variáveis para armazenar os pontos de apogeu e perigeu
distancia_max = 0
distancia_min = float('inf')
# Definindo loop
while t < 100 * 3600 * 24:
    # Calculando a distância atual
    r = (((x - xt) ** 2) + ((y - yt) ** 2)) ** 0.5  # posição da Terra
    print(r)

    # Atualizando a distância máxima e mínima
    if r > distancia_max:
        distancia_max = r
    if r < distancia_min:
        distancia_min = r

    # Calculando a aceleração
    a = (-G * M) / (r ** 3)
    ax = a * (x - xt)
    ay = a * (y - yt)

    # Atualizando velocidades
    vx += ax * dt
    vy += ay * dt

    # Atualizando posições
    yanterior = y
    x += vx * dt
    y += vy * dt

    if (yanterior <= 0) and (y > 0):
        tempo = t / 3600 / 24
        #print(f"Tempo órbita: {tempo:.4f}")

    x_lista.append(x)
    y_lista.append(y)

    # Atualizando tempo
    t += dt

# Calculando semi-eixo maior (a), semi-eixo menor (b) e excentricidade (e)
a = (distancia_max + distancia_min) / 2
b = np.sqrt(distancia_max * distancia_min)
e = np.sqrt(1 - (b ** 2 / a ** 2))
c = a * e

# Coordenadas dos focos
foco1 = (0, 0)
foco2 = (-2 * c, 0)

# Exibindo os focos
print(f"Os focos da elipse são: {foco1} e {foco2}")

def calcular_posicao():
    global x, y, vx, vy

    # Distancia entre Terra e Lua
    r = np.sqrt((x - xt) ** 2 + (y - yt) ** 2)

    # Calculando a aceleração
    a = (-G * M) / (r ** 3)
    ax = a * (x - xt)
    ay = a * (y - yt)

    # Atualizando velocidades
    vx += ax * dt
    vy += ay * dt

    # Atualizando posições
    x += vx * dt
    y += vy * dt
    #print(f'X: {x:.3f}; Y: {y:.3f}')

    return x, y

# Função para animar a órbita
def animar_orbita():
    x, y = calcular_posicao()

    # Converte as coordenadas para a escala do canvas
    escala = 2e6  # Ajuste a escala conforme necessário
    x_canvas = 300 + x / escala
    y_canvas = 300 - y / escala

    # Atualiza a posição da Lua no canvas
    canvas.coords(lua, x_canvas - 5, y_canvas - 5, x_canvas + 5, y_canvas + 5)

    # Chama a função novamente após 50 ms
    janela.after(50, animar_orbita)


# Criando a janela principal
janela = tk.Tk()
janela.title("Simulação da Órbita da Lua")

# Criando o canvas para desenhar
canvas = tk.Canvas(janela, width=600, height=600, bg="black")
canvas.pack()

# Desenhando a Terra
terra = canvas.create_oval(295, 295, 305, 305, fill="blue")

# Desenhando a Lua
lua = canvas.create_oval(295 + x / 2e6 - 5, 300 - y / 2e6 - 5, 300 + x / 2e6 + 5, 300 - y / 2e6 + 5, fill="white")

# Iniciando a animação
animar_orbita()

# Iniciando o loop principal do Tkinter
janela.mainloop()
