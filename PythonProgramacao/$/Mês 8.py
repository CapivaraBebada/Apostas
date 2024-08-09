#   Informações sobre o que tenho e gastarei
print(' ')
tenho = 1245
cartao = 196.42 + 16.05 + 83.56 + 14 + 65
cabelo = 90
UnB = 65
internet = 65
ADS = 242.94
guardar = 190
lazer = 217.02
#   Continha:
conta = cartao + cabelo + UnB + internet + ADS
conta1 = cabelo + UnB + internet + ADS
sobra = tenho - conta - guardar - lazer
total = conta + guardar + lazer
#   Informações de gastos
print(f'Dinheiro do mês: \033[4:1m{tenho}\033[m reais.')
print(f'Cartão: \033[4:1m{cartao:.2f}\033[m reais.')
print(f'Cabelo + UnB + Internet + ADS: \033[4:1m{conta1:.2f}\033[m reais.')
print('+=+=' * 20)
print(f'Conta em geral: \033[4:1m{conta:.2f}\033[m reais.')
print(f'Guardar: \033[4:1m{guardar:.2f}\033[m reais.')
print(f'Lazer: \033[4:1m{lazer:.2f}\033[m reais!!')
print(f'Total: \033[4:1m{total:.2f}\033[m reais!!')
#   Verificando se o dinheiro foi gerido da forma correta
if 0 <= sobra <= 2:
    print('\033[42:30m A conta está correta, não há dinheiro para ser gerido!\033[m')
elif sobra < 0:
    print(f'\033[41:30m Estamos no negativo por {sobra:.2f} reais \033[m')
elif sobra > 2:
    print(f'\033[30:43m Está sobrando {sobra:.2f} reais para ser gerido. '
          f'Coloque meteda em Lazer e outra metade em Guardar.\033[m')
