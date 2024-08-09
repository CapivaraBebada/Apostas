import json
import math
import tkinter as tk

# Entrada de valores
entrada = json.loads('{"vp":1022, "G":6.67430e-11, "M":5.97219e24, "m":7.34767309e22, "dt":10000, "x0":-384400000, "y0":0}')

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

def calcular_posicao():
    global x, y, vx, vy

#   Distância entre Terra e Lua
    r = ((x - xt) ** 2 + (y - yt) ** 2)**0.5
    #print(f'{r:.4f}')

    # Calculando a aceleração
    a = (-G * M) / (r ** 3)
    ax = a * (x - xt)
    ay = a * (y - yt)
    #print(f'a: {a:.4}; ax: {ax:4f}; ay: {ay:.4f}')

#   Calculando velocidades
    vx += ax * dt
    vy += ay * dt
    v = math.sqrt((vx**2) + (vy**2))
    #print(f'V: {v:.2f}:Vx: {vx:.2f}; Vy: {vy:.2f}')

#   Calculando posições
    x += vx * dt
    y += vy * dt
    #print(f'X: {x:.3f}; Y: {y:.3f}')

    return x, y


# Função para animar a órbita
def animar_orbita():
    x, y = calcular_posicao()

#   Converte as coordenadas para a escala do canvas
    escala = 2e6    # 1 pixel no canvas equivale a 2 milhões de metros
    x_canvas = 300 + x / escala
    y_canvas = 300 - y / escala

#   Atualiza a posição da Lua no canvas
    canvas.coords(lua, x_canvas - 5, y_canvas - 5, x_canvas + 5, y_canvas + 5)

#   Chama a função novamente a cada 50 ms
    janela.after(50, animar_orbita)


# Criando janela
janela = tk.Tk()
janela.title("Simulação da Órbita da Lua")

# Definindo tamanho e cor de fundo do canvas
canvas = tk.Canvas(janela, width=600, height=600, bg="black")
canvas.pack()

# Para manter o tamanho entre Terra e Lua em escala
diametro_terra = 12742000  # Diâmetro da Terra em METROS
diametro_lua = 3474000     # Diâmetro da Lua em METROS
escala = 1e6               # 1 pixel no canvas representa 1 milhâo de metros

# Convertendo metro para pixel
raio_terra_canvas = diametro_terra / escala
raio_lua_canvas = diametro_lua / escala

# Formato oval da Terra
terra = canvas.create_oval(300 - raio_terra_canvas, 300 - raio_terra_canvas,
                           300 + raio_terra_canvas, 300 + raio_terra_canvas,
                           fill="blue")

# Formato oval da Lua
lua = canvas.create_oval((300 + x / escala) - raio_lua_canvas, (300 - y / escala) - raio_lua_canvas,
                         (300 + x / escala) + raio_lua_canvas, (300 - y / escala) + raio_lua_canvas,
                         fill="white")

# Iniciar a animação
animar_orbita()

# Abrir janela de animação
janela.mainloop()
