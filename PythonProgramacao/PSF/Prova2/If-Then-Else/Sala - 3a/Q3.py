import math
s = input()
a, b, c = map(float, s.split(' '))
delta = (b ** 2) - (4 * a * c)
raiz = math.sqrt(delta)
x1 = ( (-b) + raiz ) / (2 * a)
x2 = ( (-b) - raiz ) / (2 * a)

mini = min(x1, x2)
maxi = max(x1, x2)

print(f'{mini:.4f} {maxi:.4f}')
