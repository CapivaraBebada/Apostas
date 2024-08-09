#   Escreva um programa que receba o valor das componentes x e y de um vetor bidimensional em uma mesma linha,
#separados por espaço. Retorne a frase abaixo descrevendo o vetor.

#   Dica: use o a função math.atan2 para calcular o arco tangente considerando os sinais de forma correta.

import math
s = input()
x, y = map(int, s.split(' '))
print(x, y)
#Continha:
raiz = math.sqrt(x**2 + y**2)
angulog = math.atan2(y, x)
angulor = math.degrees(angulog)
print('O vetor possui módulo {:.2f} e faz um ângulo de {:.1f}° com o eixo horizontal positivo'.format(raiz, angulor))