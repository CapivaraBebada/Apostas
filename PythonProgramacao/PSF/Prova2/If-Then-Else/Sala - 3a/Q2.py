s = input()
peso, altura = map(float, s.split(' '))
imc = peso / (altura ** 2)
imc_maior = imc - 24.9

if imc <= 18.5:
    print(f'IMC: {imc:.2f}')
    print('Baixo peso')
elif 18.5 < imc <= 24.9:
    print(f'IMC: {imc:.2f}')
    print('Peso recomendado')
elif 24.9 < imc <= 29.9:
    print(f'IMC: {imc:.2f}')
    print('Sobrepeso')
    print(f'perda recomendada: {imc_maior:.2f}')
elif 29.9 < imc <= 34.9:
    print(f'IMC: {imc:.2f}')
    print('Obeisade grau I')
    print(f'perda recomendada: {imc_maior:.2f}')
elif 34.9 < imc <= 39.9:
    print(f'IMC: {imc:.2f}')
    print('Obesidade grau II')
    print(f'perda recomendada: {imc_maior:.2f}')
else:
    print(f'IMC: {imc:.2f}')
    print('Obesidade grau III')
    print(f'perda recomendada: {imc_maior:.2f}')
