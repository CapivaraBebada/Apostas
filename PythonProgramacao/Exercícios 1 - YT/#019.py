#Faça um algoritmo que leia um valor e mostre o ângulo de seno, cosseno e tangente dele
from math import radians, sin
from math import radians, cos
from math import radians, tan
a=float(input('Digite um número: '))
s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))
print('O seno de {} é {:.2f}\nO cosseno de {} é {:.2f}\nO cosseno de {} é {:.2}'.format(a,s,a,c,a,t))