string = input()
lista = string.split(',')
float_lista = [float(x) for x in lista]
soma = sum(float_lista)
quantidade = len(float_lista)
media = soma / quantidade
print('{:.2f}'.format(media))
