# Listar valores nao pré-fixados e ordená-los
lista = []

while True:                                             # O usuário que vai ditar quantas vezes o loop se repetirá
    valor = int(input('Digite um número: '))

    if valor not in lista:                              # Colocando valores na lista
        lista.append(valor)
        print('Valor adicionado com sucesso!')

    else:                                               # Se o valor for repetido, não será adicionadpo
        print('- Valor repetido! Não adicionado!')

    resposta = input('Pretende continuar?[S/N] ')       # Escolha de continuar ou não o código

    if resposta in 'Nn':                                # Condição para parar
        break

sorted(lista)                                           # Colocando lista em ordem
print(f'Sua lista foi: {lista}')
