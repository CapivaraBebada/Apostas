s = input()
x, y = map(float, s.split(' '))
if x >= 0 and y >= 0:
    conta = x + y
    print(f'{conta:.1f}')
elif x >= 0 and y < 0:
    conta = x + (y ** 2)
    print(f'{conta:.1f}')
elif x < 0 and y >= 0:
    conta = (x ** 2) + y
    print(f'{conta:.1f}')
elif x < 0 and y < 0:
    conta = (x ** 2) + (y ** 2)
    print(f'{conta:.1f}')

