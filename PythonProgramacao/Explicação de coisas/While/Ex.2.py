n = 1
count = 0
count1 = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 ==0:
        count += 1
    else:
        count1 += 1
print('=== FIM === ')
print('Quantidade de números pares: {}\nQuanridade de números ímpares: {}'.format(count - 1, count1))