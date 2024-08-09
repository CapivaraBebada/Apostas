numero = int(input('Digite um número para calcular o fatorial: '))
count = numero
fatorial = 1
while count > 0:
    print('{}' .format(count), end=' ')
    print(' x ' if count > 1 else ' = ', end=' ')
    fatorial *= count
    count -= 1
print(fatorial)

