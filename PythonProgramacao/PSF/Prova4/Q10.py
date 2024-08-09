import math
def angulo(u, v):
    escalar = sum(u[i] * v[i] for i in range(len(u)))
    modulo_u = math.sqrt(sum(u[i] ** 2 for i in range(len(u))))
    modulo_v = math.sqrt(sum(v[i] ** 2 for i in range(len(v))))
    return math.acos(escalar / (modulo_u * modulo_v))

lista_modulo_u = input()
float_modulo_u = [float(i) for i in lista_modulo_u.split()]
lista_modulo_v = input()
float_modulo_v = [float(i) for i in lista_modulo_v.split()]

print(f'{angulo(float_modulo_u, float_modulo_v):.2f}')