# Classificação de atletas
from datetime import date
nas = int(input('Qual sua data de nascimento? '))
atual = date.today().year
idade = atual - nas

if idade <= 9:
    print('O aluno tem {} anos e está na categoria MIRIM!'.format(idade))
elif 14 >= idade > 9:
    print('O aluno tem {} anos e está na categoria INFANTIL!'.format(idade))
elif  14 < idade <= 19:
    print('O aluno tem {} anos e está na categoria JUNIOR!'.format(idade))
elif 19 < idade <= 25:
    print('O aluno tem {} anos e está na categoria SÊNIOR!'.format(idade))
elif idade > 25:
    print('O aluno tem {} anos e está na categoria MASTER!'.format(idade))
