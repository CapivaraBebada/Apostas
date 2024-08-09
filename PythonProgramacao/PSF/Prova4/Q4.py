from math import factorial

def exp2(x, n):
    soma = 0
    for i in range(0, n):
        divisao = (x ** i) / factorial(i)
        soma += divisao
    return soma
print('%.10f'%exp2(5,4))
