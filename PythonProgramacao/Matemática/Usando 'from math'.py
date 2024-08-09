from math import sqrt
numero=int(input('Digite um numero: '))
raiz=sqrt(numero)
print('A raiz de {} é {:.2f}'.format(numero, raiz))

#Na linha 3 o cálculo da raiz é feita, entao dentro do FORMAT nao precisa colocar SQRT

#Se quiser fazer o arredondamento para baixo:
from math import sqrt, floor
numero=float(input('Digite um número: '))
raiz=sqrt(numero)
print('A raiz de {} é {:.2f}'.format(numero, floor(raiz)))

#E para cima:
from math import ceil
numero=int(input('Digite um número: '))
raiz=sqrt(numero)
print('A raiz de {} é {:.2f}'.format(numero, ceil(raiz)))