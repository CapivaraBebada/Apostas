# Para uma condição ocorrer, deve haver esta forma:
# ifcarro.esquerda():
#   blocoTrue
# else
#   blocoFalse

#EXEMPLO:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
M = (n1+n2)/2
if M >= 4.59:
    print('Parabéns, sua média foi {:.2f}. Você passou de série!'.format(M))
else:
    print('Que pena, você foi burro. Sua média foi {:.2f}. Você reprovou!'.format(M))