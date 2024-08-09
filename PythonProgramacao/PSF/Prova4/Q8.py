def quadrado(x):
    if type(x) is list:
        return [ i ** 2 for i in x ]
    else:
        return x ** 2