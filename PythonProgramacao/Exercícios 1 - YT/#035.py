a = int(input('Digite um segmento de reta: '))
b = int(input('Digite outro: '))
c = int(input('Digite outro: '))
if c < a+b and a < (b+c) and b < (a+c):
    print('As retas escolhidas \033[1mformam\033[m um triângulo!')
else:
    print('As retas escolhidas \033[1mnão formam\033[m um triângulo!')