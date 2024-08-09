# Progressão aritmética
numero = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
maximo = int(input('Até quanto? '))
for c in range(numero, maximo+1, razao):
        print(c, end= ' - ')
print('ACABOU')