#Custo de uma viagem
dis = int(input('Qual a distância da viagem? '))
b = dis*(0.5)
c = dis*(0.45)
if dis <= 200:
    print('O valor da viagem ficou: {} reais'.format(b))
else:
    print('O valor da viagem ficou: {} reais'.format(c))