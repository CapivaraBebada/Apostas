# Área do quadrado, triângulo, trapézio, cilindro e círculo
print('Para o quadrado: ')
Q1 = float(input('Lado 1 do quadrado: '))
Q2 = float(input('Lado 2 do quadrado: '))
AQ = Q1*Q2
print('A área do quadrado é: {}'.format(AQ))

print('Para o triângulo: ')
T1 = float(input('Base: '))
T2 = float(input('Altura: '))
AT = (T1*T2)/2
print('A área do triângulo é: {}'.format(AT))

print('Para o trapézio: ')
B = float(input('Base maior: '))
b = float(input('Base menor: '))
H = float(input('Altura: '))
A = (((b+B)*H)/2)
print('A área do trapézio é: '.format(A))

print('Para um círculo: ')
r = float(input('Raio: '))
AC = 3.14*r
print('A área do círculo é: {}'.format(AC))

print('Para o cilindro: ')
area = float(input('Área: '))
altura = float(input('Altura: '))
C = area*altura
print('Área do cilindro: {}'.format(C))
