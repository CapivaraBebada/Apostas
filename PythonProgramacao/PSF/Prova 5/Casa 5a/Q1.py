n = int(input())

#   Quadrado da soma
quadrado_soma = sum([n for n in range(n + 1)]) ** 2
#   Soma dos quadrados
soma_quadrados = sum([n ** 2 for n in range(n + 1)])
#   Diferença
diferenca = quadrado_soma - soma_quadrados
print(diferenca)

'''
    Também pode ser feito:

def dif_quadrados(n):
    quadrado_da_soma = sum( [ n for n in range(n + 1) ] ) ** 2
    soma_dos_quadrados = sum( [ n ** 2 for n in range(n + 1) ] )
    return quadrado_da_soma - soma_dos_quadrados
print(dif_quadrados(7))
print(dif_quadrados(50))
'''