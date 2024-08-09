numero = input()
separa = numero.split(',')
float = [float(x) for x in separa]

mini = min(float)
maxi = max(float)

print('O menor valor é  {} e o maior valor é {}'.format(mini, maxi))