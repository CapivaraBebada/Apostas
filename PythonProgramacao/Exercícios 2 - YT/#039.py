# Tempo para o alistamento
nas = int(input('Qual o seu ano de nascimetno? '))
tempo = 2024 - nas
a = (-1)*(nas + 18 - 2024)
if tempo < 18:
    print('Você ainda não precisa se alistar ao exército')
elif tempo == 18:
    print('Você tem 18 anos, deve se alistar ao exército!'.format(tempo))
elif tempo > 18:
    print('Você está atrasado, já se passaram {} anos do seu alistamento'.format(a))
