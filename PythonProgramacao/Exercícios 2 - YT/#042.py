#   Novamente, os triângulos
a = int(input('RETA 1: '))
b = int(input('RETA 2: '))
c = int(input('RETA 3: '))
#'CONDICAO DE EXISTENCIA
if (a + b) >= c and (a + c) >= b and (b + c) >= a:
    print('As retas podem formar um tipo de triângulo: ', end='')
    if a == b == c:
        print('EQUILÁTERO')
    elif a == b and a != c:
        print('ISÓCELES!')
    elif a == c and c != b:
        print('ISÓCELES!')
    elif c == b and c != a:
        print('ESCALENO!')
    elif a != b != c:
        print('ESCALENO!')
else:
    print('Os valores das retas NÃO formam um triângulo!')
