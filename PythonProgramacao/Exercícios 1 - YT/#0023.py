#Separe os dígitos de um número
numero=int(input('Digite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Analizando o número {}'.format(numero))
print('A unidade desse número é: {}'.format(u))
print('A dezena desse número é: {}'.format(d))
print('A centena desse número é: {}'.format(c))
print('O milhar desse numero é: {}'.format(m))

#Não entendi a relação entre a divisão inteira e o módulo