''' Ler 5 valores numéricos, colocá-los numa lista, definir quem é maior e menor e suas respectivas posições '''

# Definindo lista vazia
lista_vazia = []
# Definindo loop para preencher a lista
for i in range(5):
    numero = int(input('Digite um número: '))
    lista_vazia.append(numero)
# Encontrando o maior e menor valor
maximo = max(lista_vazia)
minimo = min(lista_vazia)

print(f'O menor valor encontrado foi: {minimo}; e sua(s) posição(ões): ', end=' ')
# Encontrando o maior valor e sua posição:
for c, v in enumerate(lista_vazia):
    if v == minimo:
        print(f'{c}... ', end=' ')
# Para organizar o terminal
print(f'O maior valor encontrado foi: {maximo} e sua(s) poisção(ões): ', end=' ')
# Encontrando o menor valor e sua posição:
for c, v in enumerate(lista_vazia):
    if v == minimo:
        print(f'{c}...', end=' ')
print()

''''
# Encontrando suas posições
posicao_maximo = [c for c, v in enumerate(lista_vazia) if v == maximo]
posicao_minimo = [c for c, v in enumerate(lista_vazia) if v == minimo]
'''

