import math
valores = input()
x, y = map(int, valores.split(' '))
vetor = math.sqrt(x**2 + y**2)
arco_grau = math.atan2(y, x)
arco_rad = math.degrees(arco_grau)
print('O vetor possui módulo {:.2f} e faz um ângulo de {:.1f}º com o eixo horizontal.'.format(vetor, arco_rad))