# O que já foi visto:
# nome=input('Qual é o seu nome? ')
# print('Olá, {}!'.format(nome))

#Agora o que será feito:
nome=input('Qual é o seu nome? ')
print('Olá, {:10}!!!'.format(nome))
#Atenção nos pontos de exclamação

#Tambem pode ser usado:
nome=input('Qual é o seu nome? ')
print('Olá, {:>10}!!!'.format(nome))

#Ou também:
nome=input('Qual é o seu nome? ')
print('Olá, {:<10}!!!'.format(nome))

#Ou até alinhado:
nome=input('Qual é o seu nome? ')
print('Olá, {:^20}!!!'.format(nome))

#Tem isso também:
nome=input('Qual é o seu nome? ')
print('Olá, {:=^15}!!!'.format(nome))