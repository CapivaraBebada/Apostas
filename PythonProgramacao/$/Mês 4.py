# Informações sobre o que tenho e gastarei
print(' ')
tenho = 1555.42
cartao = 9.50 + 23.31 + 94.77 + 16.05 + 19.99 + 196.42 + 83.56 + 102.49 + 13
cabelo = 90
UnB = 50
internet = 65
spotify = 13
ADS = 242.94
guardar = 298.39
lazer = 250
#Continha:
conta = cartao + cabelo + UnB + internet + spotify + ADS
total = conta - guardar
sobra = tenho - conta - guardar - lazer

print('Cartão: \033[4:1m{:.2f}\033[m reais'.format(cartao))
print('Conta em geral: \033[4:1m{:.2f}\033[m reais.'.format(conta))
print('Guardado: \033[4:1m{:.2f}\033[m reais.'.format(guardar))
print('Lazer: \033[4:1m{:.2f}\033[m reais!!'.format(lazer))
print(' ')

print('Qualquer outro valor que sobre após o pagamento de tudo ou que sobre no final do mês, metade será guardado e o outro destinado a lazer')
if 0 <= sobra <= 2:
    print('A conta está correta, não há dinheiro para ser gerido!')
elif sobra < 0:
    print('Estamos no negativo por {:.2f}'.format(sobra))
elif sobra > 2:
    print('Está sobrando {:.3f} reais para ser gerido. Coloque meteda em Lazer e outra metade em Guardar.'.format(sobra))
