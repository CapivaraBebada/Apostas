nome = str(input().upper())
separa = nome.split()
ultimo_nome = separa[-1]
primeira_letra = nome[0]
print('{}, {}.'.format(ultimo_nome, primeira_letra))
