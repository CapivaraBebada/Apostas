# Empréstimo para a compra de uma casa
casa = float(input(('Qual é o valor da casa? ')))
salario = float(input('Quanto é o seu salário? '))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos*12)
minimo = salario*0.3
if minimo > salario:
    print('O empréstimo foi negado!')
elif minimo <= salario:
    print('O empréstimo foi aceito!')