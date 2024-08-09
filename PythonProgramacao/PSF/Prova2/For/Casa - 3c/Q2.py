quantas_temperaturas = int(input())
for c in range(0, quantas_temperaturas):
    celsius = float(input())
    conversao = (celsius * (9 / 5)) + 32
    print(f'{celsius} °C  {conversao:.1f} °F')