# Lisa de nomes
nome1 = input()
nome2 = input()
# Separa
separa1 = nome1.split(',')
separa2 = nome2.split(',')
# Em ordem
ordem = sorted(separa1)
# Novo item
posicao = 5
separa1.insert(posicao, separa2[0])

print(separa1)
