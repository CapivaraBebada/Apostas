# Conversão de números
import math
numero = int(input('Digite um número: '))
print('''Escolha uma das opções:
[1] CONVERTER PARA BINÁRIO
[2] CONVERTER PARA OCTAL
[3] CONVERTER PARA HEXADECIMAL''')
opcao = int(input('Escolha uma das opções: '))
if opcao == 1:
    print('O número {} convertido para binário é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('O número {} convertido para ocatal é {}'.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('O número {} convertido para hexadecial é {}'.format(numero, hex(numero)[2:]))
else:
    print('Será aceita apenas opcões entre 1 e 3')

    # Ao final de cada print nas condições determina que as letras, quando os números são convertidos, não apareçam