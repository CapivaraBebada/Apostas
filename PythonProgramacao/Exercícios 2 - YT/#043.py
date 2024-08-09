#   Cálculo do IMC
peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
h = altura**2
imc = (peso / h)
if imc < 18.5:
    print('O IMC desta pessoa é de {:.2f}km/m². Logo, ela está ABAIXO do peso.')
elif 18.5 <= imc < 25:
    print('O IMC desta pessoa é de {:.2f}km/m². Logo, ela está na sua faixa de peso.'.format(imc))
elif 25 <= imc < 30:
    print('O IMC desta pessoa é de {:.2f}km/m². Logo, ela está na faixa de SOBREPESO.'.format(imc))
elif 30 <= imc < 40:
    print('O IMC desta pessoa é de {:.2f}km/m². Logo, ela está na faixa de OBESIDADE.'.format(imc))
elif imc >= 40:
    print('O IMC desta pessoa é de {:.2f}km/m². Logo, el está na faixa de OBESIDADE MÓRBIDA.'.format(imc))
