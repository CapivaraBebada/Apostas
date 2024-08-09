# Média de notas
nota1 = float(input('Nota da primeira prova: '))
nota2 = float(input('Nota da segunda prova: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('O aluno está reprovado!')
elif 5 <= media <= 6.9:
    print('O aluno está de recuperação')
elif media >= 7:
    print('O aluno foi aprovado!')
