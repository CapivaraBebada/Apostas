def quadrado(x):
    if type(x) is list:
        return [(numero ** 2) for numero in x]
    else:
        return x ** 2