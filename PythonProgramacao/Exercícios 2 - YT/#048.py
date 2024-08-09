# Soma de todos os números ímpares que são múltiplos de 3
soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print('A soma de todos os {} valores é {}'.format(cont, soma))