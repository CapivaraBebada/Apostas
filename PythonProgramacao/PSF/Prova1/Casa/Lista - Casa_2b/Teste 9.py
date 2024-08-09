lista_string = input()
separa_string = lista_string.split(',')
lista_float = [float(x) for x in separa_string]
mini = min(lista_float)
maxi = max(lista_float)
print(mini)
print(maxi)
