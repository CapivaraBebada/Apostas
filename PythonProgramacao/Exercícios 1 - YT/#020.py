#Sortear um aluno, entre quatro, e mostrar o nome do aluno sorteado
import random
a=input('Aluno1: ')
b=input('Aluno2: ')
c=input('Aluno3: ')
d=input('Aluno4: ')
lista=[a,b,c,d]
e=random.choice(lista)
print('O aluno sorteado foi: {}'.format(e))