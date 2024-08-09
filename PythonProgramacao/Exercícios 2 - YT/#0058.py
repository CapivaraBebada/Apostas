import random
print('Sou o seu computador...\nAcabei de pensar em um número de 0 a 10\nVocê consegue adivinhar qual foi?')
comp = random.randint(0,5)
acertou = False
palpite = 0
while not acertou:
    jogador = float(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == comp:
        acertou = True
        print('Parabéns, voce acertou o número {} com {} tentativas'.format(comp, palpite))
    elif jogador < comp:
        print('Escolha um número mais alto. Tente novamente! ')
    elif jogador > comp:
        print('Escolha um número mais baixo. Tente novamente! ')
