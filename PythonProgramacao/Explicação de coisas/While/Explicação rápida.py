# Diferentemente do 'for' o while serve para estruturas  de repetição em que você não tem um limite pré-definido

#   Sabendo o limite:
print('=== Exemplo 1 ===')
c = 1
while c < 4:
    print(c)
    c += 1
print('Fim!')
print(' ')

#   Não sabendo o limite:
print('=== Exemplo 2 ===')
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim!')
print(' ')

