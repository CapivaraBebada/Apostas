lista = []
for i in range(5):
    numero = int(input('Digite um numero: '))

    if i == 0:                                # Se o número ofor o primeiro valora ser adicionado
        lista.append(numero)

    elif numero > lista[-1]:                  # Se o numero adicionado for maior do que o último elemento da lista
        lista.append(numero)

    else:
        posicao = 0                           # Recebe valor 'zero' para varrer toda a lista
        while posicao < len(lista):           # Se o valor da posição é menor do que o tamanho da lista
            if numero <= lista[posicao]:      # Se o número digitado é menor do que o número no valor da posição especí.
                lista.insert(posicao, numero) # Adiciona o número em uma posição específica
                break
            posicao += 1                      # A varredura acontecerá até a posição ser menor do que o tamamho da lista
print('+=' * 27)
print(f'Os valore digitados, em ordem, foram: {lista}')
