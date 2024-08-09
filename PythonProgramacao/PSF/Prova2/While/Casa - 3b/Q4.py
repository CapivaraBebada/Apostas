#   Numero de repetições
n = int(input())
#   Pontos iniciais e finais
a = 0
b = 3
#   Media
delta_x = (b - a) / n
#   Proximo ponto
x = a
#   Numero de somas
soma = 0
#   Numero de repeticoes
i = 1
#   Loop
while i <= n:
    xi = a + (i * delta_x)
    soma += ( (xi ** 3) - (6 * xi) ) * delta_x
    i += 1
print(soma)