def  fatorialN(n):
    soma = 1
    for i in range(1, n +1):
        soma *= i
    return soma
print(fatorialN(9))

