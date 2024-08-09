# Inserir um nome a uma lista usando INSERT
nome = input()
novo_nome = input()
# Posição:
posicao = 5
# Separando e adicionando
lista = nome.split(',')
lista.insert(posicao, novo_nome)

print(lista)

