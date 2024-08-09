#Leia se um número é ímpar ou par
num = int(input('Digite um número: '))
di = num % 2
resto = 0
if di == resto:
    print('O número {} é \033[1mpar\033[m.'.format(num))
else:
    print('Número {} é \033[1mímpar\033[m.'.format(num))
