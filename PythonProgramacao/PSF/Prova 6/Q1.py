import json
# Definindo entrada
entrada = json.loads(input())
# Sequencia de valores e variaveis
y0 = entrada['y0']
vy0 = entrada['vy0']
m = entrada['m']
g = entrada['g']
k = entrada['k']
dt = entrada['dt']
t = []
y = y0
# Definido loop
while y > 0:
    y = y0 + vy0 * dt
    vy = vy0 + (- g - (k/m) * abs(vy0) * vy0) * dt
    y0 = y
    vy0 = vy
    t.append(dt)
print(f'{sum(t):.1f}')