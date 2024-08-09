# Mais leve e mais pesado
maior = 0
menor = 0

for pessoa in range(1,6):
    peso = float(input('Peso da pessoa {}: '.format(pessoa)))
    if peso > maior:
        peso1 = peso
    elif peso < menor:
        peso2 = peso
print('O maior peso lido foi: {} kg\nE o menor peso lido foi: {} kg'.format(peso1, peso2))
