frase = input()
separa = frase.split()
inverte = []
#   Criando um loop
for i in range(len(separa) -1, -1, -1):
    inverte.append(separa[i])

for j in inverte:
    print(j)
