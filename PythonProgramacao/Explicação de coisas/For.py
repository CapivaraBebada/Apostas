# Laço: faz com que uma determinada estrutura se repita quantas vezes quiser
# O que será repetido deverá estar dentro da estrutura, assim como o uso do 'if'
# A contagem não inclui o último número, portanto ser for colocado o número 6, será repetido 5 vezes

print('Exemplo1:')
for c in range (0, 3):  #->  seria a quantidade de vezes repetidas
    print('Oi')
# quando for printado, a frase repetirá a quantidade de vezes pedida

print('Exemplo2:')
# se o comando for para printar o próprio "c", então ele repetirá os números que estão entre parênteses
# lembre-se que o último é ignorado
for c in range(1, 5):
    print(c)

print('Exemplo3:')
# com o -1 ao final, significa que a contagem será do maior para o menor
for c in range(4, 0, -1):    #atenção na ordem dos números!!!
    print(c)

print('Exemplo4:')
# com o terceiro número, significa que a contagem será alternada de acordo com o número colocado até o fim
for c in range(0, 10, 3):
    print(c)

print('Exemplo5:')
# contagem alternada de cima para baixo
for c in range(6, 0, -2):
    print(c)

print('Exemplo6:')
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)

print('Exemplo7:')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim!')

print('Exemplo8:')
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório deles foi {}'.format(s))
