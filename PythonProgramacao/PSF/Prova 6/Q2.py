import json
# Definindo entrada
entrada = json.loads(input())
# Defiinindo variaveis
y0 = entrada['y0']
vy0 = entrada['vy0']
g = entrada['g']
m = entrada['m']
k = entrada['k']
dt = entrada['dt']
# Inicializando variaveis
t = 0
y = y0
altura_maxima = y0
tempo_alt_max = 0
vy = vy0
# Definindo loop
while y > 0:
    y = y + vy * dt
    vy = vy + ( - g - (k/m) * vy * abs(vy) ) * dt
    t += dt
    # Verificando quando atinge a altura maxima
    if y > altura_maxima:
        altura_maxima = y
        tempo_alt_max = t

tempo_total = t

print(f'Tempo total: {tempo_total:.2f} s')
print(f'Tempo de altura máxima: {tempo_alt_max:.2f} s')
print(f'Altura máxima: {altura_maxima:.2f} m')

# {"y0":1, "vy0":30, "g":9.82, "m":1, "k":0.0, "dt":0.001}
