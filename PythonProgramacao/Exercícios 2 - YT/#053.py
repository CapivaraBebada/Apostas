frase = str(input('Digite uma frase: ')).strip().upper()
separa = frase.split()
junta = ''.join(separa)
inverte = ''
for letra in range(len(junta) - 1, -1, -1): # o numero de letras é subtraído por 1; vai até a letra da posicao 0 e volta cada letra de tras para frente
    inverte += junta[letra]
if inverte == junta:
    print('A frase: {}; é um palíndromo'.format(frase))
else:
    print('A frase {}; não é um palíndromo.'.format(frase))
