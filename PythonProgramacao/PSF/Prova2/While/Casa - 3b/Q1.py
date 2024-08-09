numero = int(input())
divisor = 1
while divisor <= numero:
    if numero % divisor == 0:
        print(divisor)
        divisor += 1
    else:
        divisor += 1