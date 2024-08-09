import json

# Valores variáveis
tenho = float(input('Quanto terá para mês? '))
cartao = float(input('Quanto foi gasto de cartão? '))  # 348.03
unb = float(input('Quanto será gasto para a UnB? '))   # 0
# Valores imutáveis
entrada = json.loads('{"claro": 65, "cabelo": 90, "ADS": 262.61}')
# Acessadno cada elemento do dicionário
claro = entrada['claro']
cabelo = entrada['cabelo']
ads = entrada['ADS']
# Análise de dados
gastos = claro + cabelo + ads + cartao + unb
sobra = tenho - gastos
lazer = sobra / 3
guardar = (2 * sobra) / 3
confere = guardar + lazer + gastos
# Mostrando valores
print('+=+' * 20)
print(f'Apenas CARTÃO: {cartao}')
print(f'Gasto total: {gastos:.2f}')
print(f'Sobra: {sobra:.2f}')
print(f'Lazer: {lazer:.2f}')
print(f'Guardar: {guardar:.2f}')
print(f'+=+' * 20)
print(f'Conferindo conta: {confere:.2f}')
print(' ')
