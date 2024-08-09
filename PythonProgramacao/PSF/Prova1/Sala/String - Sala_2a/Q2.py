# Ultimo nome e primeira letra do nome
nome = input()
separar = nome.split()
ultimo_nome = separar[-1]
primeira_letra = nome[0]
print('{}, {}.'.format(ultimo_nome, primeira_letra))