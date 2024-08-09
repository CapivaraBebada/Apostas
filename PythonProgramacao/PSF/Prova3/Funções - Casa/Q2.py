def fatorialN(n, N=1):
    resultado = 1
    for numero in range(1, n+1, N):
        resultado *= numero
        return resultado
