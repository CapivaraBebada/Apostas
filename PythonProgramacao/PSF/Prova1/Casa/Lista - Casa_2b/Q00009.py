string = input()
separa = string.split(',')
floats = [float(x) for x in separa]
print('O maior valor: {}\nO menor valor é: {}'.format(max(floats), min(floats)))
