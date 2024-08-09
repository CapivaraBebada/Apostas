nome = input()
separa_nome = nome.split()
ordem = sorted(separa_nome)

novo = input()
separa_novo = novo.split()
posicao = 6

ordem.insert(posicao, separa_novo[0])

print(ordem)
