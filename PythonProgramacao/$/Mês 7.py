#   Informações sobre o que tenho e gastarei
print(' ')
tenho = 1300
cartao = 196.42 + 16.05 + 83.56 + 88 + 65
spot = 14
cabelo = 35
UnB = 35
internet = 65
ADS = 262.94
guardar = 234
lazer = 205
#   Continha:
conta = cartao + cabelo + UnB + internet + ADS + spot
conta1 = cabelo + UnB + internet + ADS
sobra = tenho - conta - guardar - lazer
total = conta + guardar + lazer
#   Informações de gastos
print('Dinheiro do mês: \033[4:1m{}\033[m reais'.format(tenho))
print('Cartão: \033[4:1m{:.2f}\033[m reais'.format(cartao))
print('Cabelo + UnB + Internet + ADS: \033[4:1m{:.2f}\033[m reais.'.format(conta1))
print('+=+=' * 20)
print('Conta em geral: \033[4:1m{:.2f}\033[m reais.'.format(conta))
print('Guardar: \033[4:1m{:.2f}\033[m reais.'.format(guardar))
print('Lazer: \033[4:1m{:.2f}\033[m reais!!'.format(lazer))
print('Total: \033[4:1m{:.2f}\033[m reais!!'.format(total))
#   Verificando se a conta está correta
if 0 <= sobra <= 2:
    print('\033[42:30m A conta está correta, não há dinheiro para ser gerido!\033[m')
elif sobra < 0:
    print('\033[41:30m Estamos no negativo por {:.2f} reais \033[m'.format(sobra))
elif sobra > 2:
    print('\033[30:43m Está sobrando {:.2f} reais para ser gerido. Coloque meteda em Lazer e outra metade em Guardar. \033[m'.format(sobra))
print(' ')