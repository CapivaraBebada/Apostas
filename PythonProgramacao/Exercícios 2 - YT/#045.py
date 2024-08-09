# Pedra, papel, teosoura
opcoes = print('''Qual é a sua escolha?
[0] Pedra
[1] Papel
[2] Tesoura''')
escolha = int(input('Qual é a sua jogada? '))
import time
import random
time.sleep(0.75)
print('LÁ VAI...')
time.sleep(1.15)
print('JO')
time.sleep(0.75)
print('KEN')
time.sleep(1)
print('PO!!')
time.sleep(1)
comp = random.randint(0, 2)
print('==='*5)
#A pessoa escolhe
if escolha == 0:
    print('Você escolheu PEDRA')
elif escolha == 1:
    print('Você escolheu PAPEL')
elif escolha == 2:
    print('Voce escolheu TESOURA')
elif 0 < escolha or escolha >=4:
    print('Você escolheu uma opção inválida. Jogue novamente!!!')
time.sleep(1)
#O computador escolhe
if comp == 0:
    print('O computador escolheu PEDRA')
elif comp == 1:
    print('O computador escolheu PAPEL')
elif comp == 2:
    print('O computador escolheu TESOURA')
print('==='*5)
time.sleep(1.5)
#Quem ganhou?
if escolha == comp:
    print('EMPATADO. Tente novamente!')
elif escolha == 0 and comp == 1:
    print('O COMPUTADOR GANHOU!!!')
elif escolha == 0 and comp == 2:
    print('VOCÊ GANHOU!!!')
elif escolha == 1 and comp == 0:
    print('VOCÊ GANHOU!!!')
elif escolha == 1 and comp == 2:
    print('VOCÊ GANHOU!!!')
elif escolha == 2 and comp == 0:
    print('O COMPUTADOR GANHOU!!!')
elif escolha == 2 and comp == 1:
    print('VOCE GANHOU!!!')
