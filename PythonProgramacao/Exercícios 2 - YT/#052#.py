# Prove que o número é primo ou não
numero = int(input('Digite um número: '))
count = 0
for c in range(1, numero+1):
        if numero % c == 0:
            count += 1
            print('\033[4:1m{}\033[m'.format(c), end=' ')
        else:
            print('{}'.format(c), end=' ')
if count <= 2:
    print('\nO número {} é divisível apenas por 1 e por ele mesmo, logo, é primo!'.format(numero))
else:
    print('\nO número {} é divisível por {} números, logo, não é primo!'.format(numero, count))


