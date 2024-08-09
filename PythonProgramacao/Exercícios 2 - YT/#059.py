import time
numero1 = int(input('Digite un número: '))
numero2 = int(input('Digie outro: '))
escolha = 0
while True:
    while escolha != 5:
        print('''        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa''')
        escolha = int(input('>>> O que você quer fazer? '))

        if escolha == 1:
            soma = numero1 + numero2
            print('A soma é: {} + {} = {}'.format(numero1, numero2, soma))
            print('==' * 20)

        elif escolha == 2:
            mult = numero1 * numero2
            print('A multiplicação é: {} x {} = {}'.format(numero1, numero2, mult))
            print('==' * 20)

        elif escolha == 3:
            maxi = max(numero1, numero2)
            print('O maior entre {} e {} é {}'.format(numero1, numero2, maxi))
            print('==' * 20)

        elif escolha == 4:
            print('Informe os números novamente:')
            print('==' * 20)

        elif 0 >= escolha >= 6:
            print('Erro, escolha um número entre as opções')
            print('==' * 20)

        elif escolha == 5:
            print('==' * 20)
            print('Finalizando!')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('Código finalizado com sucesso!!')
            break