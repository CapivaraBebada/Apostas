import math
import numpy
n = int(input())
massa = 9.1093837015E-31
carga = 1.602176634E-19
vacuo = 8.8541878128E-12
plank = 1.054571817E-34
pi = math.pi

num = (-1) * massa * (carga**4)
div = 2 * ((4 * pi * vacuo * plank * n)**2)

conta = num / div
conversao = conta * 6.242E+18
print('%.2e'%conta,'J')
print('{:.2f} eV'.format(conversao))
