soma1 = 0
cont1 = 0
for c in range(1, 7):
    n1 = int(input('Digite o {}º número: '.format(c)))
    if n1 % 2 == 0:
        soma1 += n1
        cont1 += 1
print('A soma dos {} valores pares é {}'.format(cont1, soma1))

