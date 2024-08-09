# Brevemente sobre Tuplas:
'''
    Exemplo:
    lanche = ('a','b','c')
        para acessar os valores, a posição inicil é o 0 (zero)
    Para tuplas, é imutável a sua variável, e para alterar algum
elemento, devemos usar uma lista. '''

# Para adicionar algum elemnto na lista, devemos usar a função "append"
print('Exemplo para adicionar elemento à lista:')
print(' ')
coisas = input('Uma lista está criada!\nDigite algo para adicionar a ela: ')
total = []
total.append(coisas)
print(total)
print(' ')
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# Para adicionar elemtento em um posição específica
lista = [1,2,3,4,5,6,7,8,9,10]
print('Agora para colocar um número em uma posição específica.')
numero = int(input('Digite um número: '))
posicao = int(input('Digite a posição do número: '))
lista.insert(posicao, numero)
print(lista)
print(' ')
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

# Para apagar ou ordenar
lista1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print('Agora para apagar posicões e números.')
numero1 = int(input('Posição do número a ser apagado(0-19): '))
del lista1[numero1]                                     # ---> Remove posição
print(f'Posição removida: {lista1}')
print(' ')
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

numero2 = int(input('Posição do número a ser apagadao(0,19): '))
lista2.pop(numero2)                                     # --->  Remove posição
print(f'Posição removida: {lista2}')
print(' ')
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

numero3 = int(input('NÚMERO a ser removido(1-20): '))   # --->  Remove variável
lista3.remove(numero3)
print(f'Número removido: {lista3}')
print(' ')
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

print('Crie uma lista entre dois números.')
n1 = int(input('Valor inicial: '))
n2 = int(input('Valor final: '))
valores = list(range(n1, n2))
print(valores)
print(' ')

print('Colocando uma lista em ordem crescente e decrescente.')
lista5 = input('Escreva numeros separados por vírgulas: ').split(',')
[int(x) for x in lista5]

lista5.sort()                                   # ---> Ordenar uma lista
print(f'Lista5 em ordem CRESCENTE:: {lista5}')

lista5.sort(reverse=True)                       # ---> Ordenar de forma inversa
print(f'Lista6 em ordem DECRESCENTE: {lista5}')
print(f'A quantidade de elementos na lista é: {len(lista5)}')
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

print('Usando for')
numero4 = input('Digite valores separados por vírgula: ').split(',')
lista_nova = [int(x) for x in numero4]
for c, v in enumerate(lista_nova):              # ---> c: índice, pocicao; v: valor da posição
    print(f'Na posição {c} encontrei {v}.')
print('Final da lista')
# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

print('Usando "input" dentro do "for".')
print(' ')
lista_vazia = []
for _ in range(0,5):
    lista_vazia.append(int(input('Digite um valor: ')))
for c, v in enumerate(lista_vazia):
    print(f'Na posição {c} há o número {v}.')

# +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-++-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
'''
Ao escrever uma variavel que recebe uma lista e logo em seguida igualá-la a uma outra variável e colocar para
printar ambas, as duas variéveis serão iguais. Para encerrar com essa ligação entre elas, faça o seguinte:          
'''
valor_2 = input('Escreva números separados por vírgula: ').split(',')
converte_2 = [int(x) for x in valor_2]
lista_nova = converte_2[:]  # Aqui foi feita uma cópia da primeira lista
numero_novo = int(input('Escreva um outro para modificar o último número da lista: '))
lista_nova[-1] = numero_novo
print(f'Lista original: {converte_2}\nLista modificada: {lista_nova}')

