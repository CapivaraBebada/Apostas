lista_vazia = []
par = []
impar = []

while True:
    numero = int(input('Digite um número: '))
    divisao = numero % 2
    if divisao == 0:
        par.append(numero)
    else:
        impar.append(numero)

    lista_vazia.append(numero)
    pergunta = input('Quer continuar? [S/N] ')

    if pergunta in 'Nn':
        break

print(f'A lista completa é: {lista_vazia}')
print(f'A lista de númmeros pares é: {par}')
print(f'A lista de números ímpares é: {impar}')
