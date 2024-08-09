import cmath
import math
s = input(' ')
x, y = map(int, s.split(' '))
com = complex(x, y)
seno = cmath.sin(com)
raiz = cmath.sqrt(3 * seno)
print('A parte real é {:.2f} e a imaginária é {:.2f}'.format(raiz.real, raiz.imag))
