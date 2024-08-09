def modvetor(u):
    potencia = [ i ** 2 for i in u ]
    return ( sum(potencia) ** 0.5 )

lista = int(input())
float_lista = [ float(i) for i in lista ]