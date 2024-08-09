from random import randint
from time import sleep

comp = randint(0, 5)
print('Pensarei em um número... Tente adivinhar qual é esse número.')
print('===' * 20)
sleep(1.5)
print('Processando... ')
print('===' * 20)
sleep(2)

while True:
    joueur = int(input('Tente adivinhar: '))

    if joueur < comp:
        print('É um número maior, tente novamente.')
    elif joueur > comp:
        print('É um número menor, tente novamente.')
    else:
        print('Parabéns, o número que eu pensei foi {}'.format(comp))
        break