numero_alunos = int(input())
dicionario = {}

for c in range(numero_alunos):
    nome = input()
    nota = float(input())
    dicionario[nome] = nota
print(dicionario)
