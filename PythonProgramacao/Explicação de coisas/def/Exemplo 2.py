#    Exemplo 2:

def numero(n):
    a, b = [0, 1]
    while a < n:
         print(a, end=' ')
         a, b = b, a + b

    print(n)

while True:
    m = int(input())
    if m < 0:
        break
    else:
        numero(m)