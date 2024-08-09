# Tabuada de qualquer número
a = int(input('Digite um número para saber sua tabuada: '))
for c in range(0, 11):
    print('{} x {} = {}'.format(a, c, a*c))