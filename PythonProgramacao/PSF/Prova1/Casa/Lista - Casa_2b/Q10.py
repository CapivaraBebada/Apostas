numeros = input()
separa = numeros.split(',')
floats = [float(x) for x in separa]
quantos = len(separa)
soma = sum(floats)
media = soma / quantos
print('média {}'.format(media))
