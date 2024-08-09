#   O programa faala qual é o maior e o menor número entre 3
n1 = int(input('Digite o primeiro valor:  '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro: '))
# Para o menor:
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
# Para o maior:
maior = n2
if n1>n2 and n1>n3:
    manior = n1
if n3>n2 and n3>n1:
    maior = n3
print('O \033[1mmenor\033[m número é {}'.format(menor))
print('O \033[1mmaior\033[m número é {}'.format(maior))

