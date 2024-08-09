#   Formas de pagamento
preco = float(input('Preço das compras: R$'))
pag = print('''Formas de pagamento: 
[1] Á vista dinheiro
[2] À vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
print(' ')
escolha = int(input('Qual a forma de pagamento? '))
#Cálculo
dinheiro = preco - (preco * 0.1)
cartao = preco - (preco * 0.05)
duas = preco
tres = preco + (preco * 0.3)
#Condiçoes
if escolha == 1:
    print('Sua compra foi de {} reais, mas custará {} reais.'.format(preco, dinheiro))
elif escolha == 2:
    print('Sua compra foi de {} reais, mas custará {} reais'.format(preco, cartao))
elif escolha == 3:
    print('Sua compra foi de {} reais'.format(preco))
elif escolha == 4:
    a = int(input('Será parcelada em quantas vezes? '))
    parcela = preco / a
    if a <= 3:
        print('Erro. Tente novamente!')
    elif a >= 4:
        print('Sua compra foi parcelada em {}x de R${}'.format(a, parcela))
        print('Sua compra de R${} passrá a custar R${}'.format(preco, tres))
else:
    print('Opção de pagamento inválida! Tente novamente.')





