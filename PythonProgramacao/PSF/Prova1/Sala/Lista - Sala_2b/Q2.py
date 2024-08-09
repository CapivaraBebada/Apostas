string = input()
lista = string.split(',')
float_lista = [float(x) for x in lista]
#Maximo e Mínimo:
maxi = max(float_lista)
mini = min(float_lista)
print('Menor valor: {:.2f}\nMaior valor: {:.2f}'.format(mini, maxi))