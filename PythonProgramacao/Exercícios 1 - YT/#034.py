# Valor do salário e seu devido aumento
sa = float(input('Digite seu salário: '))
acima = (sa*0.1)+sa
abaixo = (sa*0.15)+sa
if sa >= 1.250:
    print('O seu reajuste salarial foi para {} reais'.format(acima))
else:
    print('O seu reajuste salarial foi para: {} reais'.format(abaixo))