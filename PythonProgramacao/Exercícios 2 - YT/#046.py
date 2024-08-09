# Contagem regressiva
from time import sleep
for c in range(10, -1, -1):
    print('{}'.format(c, [sleep(1)]))
print('BUM! PÁ! POW!')