a, b = 0, 1
numero = int(input())

while numero > 0:
    sequencia = [a, b]
    while sequencia[-1] <= numero:
        proximo_valor = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_valor)
    print(sequencia[:-1])       # SELECIONAR TODOS OS ELEMENTOS DA LISTA, EXCETO O ÚLTIMO!!
    numero = int(input())