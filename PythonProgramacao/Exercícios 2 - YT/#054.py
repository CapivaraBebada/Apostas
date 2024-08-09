import datetime
import time
data = datetime.datetime.now().year
count = 0
count1 = 0

for ano in range(1, 8):
    ano = int(input('Em que ano a {}° nasceu? '.format(ano)))
    idade = data - ano
    if idade >= 18:
        count += 1
    else:
        count1 += 1
print('Quantidade de pessoas \033[4:1mmaiores\033[m de idade: {}\nQuantidade de pessoas \033[4:1mmenores\033[m de idade: {}'.format(count, count1))
