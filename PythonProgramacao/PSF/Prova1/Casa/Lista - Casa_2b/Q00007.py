nome = input()
separa = nome.split(',')
palavra = 'Jorginho'
separa.remove(palavra)
del separa[4]
ultimo = separa.pop(-1)
print(ultimo)
print(', '.join(separa))
