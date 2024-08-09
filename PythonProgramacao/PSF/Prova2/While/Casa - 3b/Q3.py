a, b = 0, 1
numero = int(input())

while numero > 0:
    lista = [a, b]
    while lista[-1] <= numero:
        proximo_valor = lista[-1] + lista[-2]
        lista.append(proximo_valor)
    print(lista[:-1])
    numero = int(input())
