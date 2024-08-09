#Qual é a área de uma parede e quanto de tinta precisa para pintá-la sendo que 1 litro pinta 2m²?

a=float(input('Qual é a largura? '))
b=float(input('E a altura? '))
A=a*b
q=a/2
print('A área da parede é: {:.2f} m².'.format(A))
print('A quantidade de tinta necessária será de: {:.2f} L.'.format(q))