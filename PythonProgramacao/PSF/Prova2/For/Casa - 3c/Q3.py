quantos_alunos = int(input())
dicionario = {}
for nome in range(quantos_alunos):
    nome = input()
    nota = float(input())
    dicionario[nome] = nota
print(dicionario)