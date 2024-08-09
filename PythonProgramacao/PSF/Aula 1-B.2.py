#Escreva um programa que receba uma string com hora, minuto e segundo, separados por dois pontos (:)
#e devolva o valor em minutos com 2 casas decimais, conforme o exemplo abaixo.

s = input()
x, y, z= map(int, s.split(':'))

#Conta:
min = (x*60) + y + z/60
print('{:.2f} min'.format(min))