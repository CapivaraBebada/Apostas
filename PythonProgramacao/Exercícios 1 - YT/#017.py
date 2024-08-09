#Ao digitar um número real, o algoritmo me devolve a sua parte inteira
from math import floor
a=float(input('Digite um número: '))
p=floor(a)
print('A parte inteira do número {} é {}'.format(a,p))