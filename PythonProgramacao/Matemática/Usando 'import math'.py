import math
numero=int(input('Digite um número: '))
raiz=math.sqrt(numero)
print('A raiz de {} é {:.3f}'.format(numero,raiz))

#para arredondar para cima ou para baixo:
numero=int(input('Digite um numero: '))
raiz=math.sqrt(numero)
print('A raiz de {} arredondado para cima é {:.2f}'.format(numero, math.ceil(raiz)))

#Já para baixo:
numero=int(input('Digite um número: '))
raiz=math.sqrt(numero)
print('A raiz de {} arredondado para baixo é {:.2f}'.format(numero, math.floor(raiz)))