import math

multiplica = 1

while True:
    numero = int(input())

    if numero < 0:
        break

    for c in range(1, numero + 1):
        multiplica *= c
    print(multiplica)