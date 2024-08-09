def fatorialN(n, N=1):
    resultado = 1
    for i in range(1, n+1, N):
        resultado *= i
    return resultado

print(fatorialN(9))