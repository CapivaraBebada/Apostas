nome = input()
separa = nome.split()
ultimo_nome = separa[-1]
primeira_letra = nome[0]
segunda_letra = separa[1][0]
print('{}, {}.{}.'.format(ultimo_nome, primeira_letra, segunda_letra))