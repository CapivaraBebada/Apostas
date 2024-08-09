soma = 0
for pessoa in range(1, 5):
    print('=== Pessoa {} ==='.format(pessoa))
    nome1 = input('NOME: ')
    idade = float(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    print(' ')
    soma += idade
    media_idade = soma / 4
print('A media de idade é {}'.format(media_idade))
#Nao sei como prosseguir

