# Informações sobre o que tenho e gastarei
print(' ')
tenho = 1500
cartao = 196.42 + 16.05 + 23.31 + 94.77 + 102.49 + 83.56 + 88.10 + 27.90 # ---> 88 SERIAM DA CALÇA!!
cabelo = 90
UnB = 50
internet = 65.90
ADS = 242.94
guardar = 209.73
lazer = 208.82
#Continha:
conta = cartao + cabelo + UnB + internet + ADS
total = conta - guardar
sobra = tenho - conta - guardar - lazer

print('Dinheiro do mês: \033[4:1m{}\033[m reais'.format(tenho))
print('Cartão: \033[4:1m{:.2f}\033[m reais'.format(cartao))
print('Conta em geral: \033[4:1m{:.2f}\033[m reais.'.format(conta))
print('Guardado: \033[4:1m{:.2f}\033[m reais.'.format(guardar))
print('Lazer: \033[4:1m{:.2f}\033[m reais!!'.format(lazer))

if 0 <= sobra <= 2:
    print('\033[42:30mA conta está correta, não há dinheiro para ser gerido!\033[m')
elif sobra < 0:
    print('\033[41:30mEstamos no negativo por {:.2f}\033[m'.format(sobra))
elif sobra > 2:
    print('\033[30:43mEstá sobrando {:.2f} reais para ser gerido. Coloque meteda em Lazer e outra metade em Guardar.\033[m'.format(sobra))
