  # Criar um programa com as seguintes funcionalidades:
# Nome com todas as letras maiúsculas.
# Nome com todas as letras minúsculas.
# Quantidade de letras sem considerar espaços.
# Quantas letras têm o primeiro nome.

nome = input('Digite seu nome: ').strip()
print('Seu nome com letras maiúsculas é: {}.'.format(nome.upper()))
print('Seu nome com letras minúsculas é: {}.'.format(nome.lower()))
print('Sem considerar os espaços, seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))

# O '.strip' na linha sete ignora os espaços depois ou antes das palavras.
# Na linha 10 o espaço entre o nome não são contados.
# Na linha 13 está contando quantos espaços foram usados até o espaço estre os nomes, ou seja, a quantidade de letras do
#do primeiro nome.