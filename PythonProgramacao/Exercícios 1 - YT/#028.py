# Fazer tentar adivinhar em que número o computador "pensou"
from random import randint
comp = randint(0, 1000) # Aqui o computador sorteia
print('===' * 20)
print('Vou pensar em um número. Tente adivinhar... ')
print('===' * 20)
jouer = int(input('Em que número pensei? ')) # Aqui o jogador tenta adivinhar
if jouer == comp:
    print('Parabéns, você acertou. Pensei no número {}'.format(jouer))
else:
    print('Tente mais uma vez... ')
