# Escreva um programa que leia a parte real e a parte imaginária de um número complexo z separadas por espaço.
# Calcule o resutado da expressão sqrt(3sin(z))
# Retorne a parte real e a parte imaginária do resultado, com 2 casas decimais depois da vírgula.

# Dica 1: Leia as partes real e imaginaria como números de ponto flutuante
# e use o comando complex para criar uma variável complexa a partir das suas partes real e imaginária.
# Dica 2: Use o modulo cmath ou o módulo numpy para calcular o seno de um número complexo.

#   Input	Result
#   3 4
#   6.83 -5.93

import math
import cmath
s = input()
x, y = map(int, s.split(' '))
z = complex(x, y)
seno = cmath.sin((z))
raiz = cmath.sqrt(3*seno)
print('{:.2f} {:.2f}'.format(raiz.real, raiz.imag))

