#Leia se um ano é bissexto ou não
num = int(input('Digite o algarismo de um ano: '))
div = num % 4
resto = 0
if div == resto:
    print('O ano \033[1:4m{}\033[m \033[1:4mé\033[m ano bissexto!'.format(num))
else:
    print('O ano \033[4:1m{}\033[m \033[1:4mnão\033[m é ano bissexto!'.format(num))