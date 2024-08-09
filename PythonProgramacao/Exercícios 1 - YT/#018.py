#Faça o cálculo da hipotenusa sabendo o valor de seus catetos
import math
cat1=float(input('Valor do cateto1: '))
cat2=float(input('Valor do cateto2: '))
hi=math.hypot(cat1,cat2)
print('O valor da hipotenusa é: {:.2f}'.format(hi))

#Também pode ser feito desta forma:
from math import hypot
cat1=float(input('Qual é o valor do cateto1? '))
cat2=float(input('Qual é o valor do cateto2? '))
h=hypot(cat1, cat2)
print('A hipotenusa vale: {:.2f}'.format(h))