#Formas para o sistema escolher um número aleatório:
'''import random
numero=random.random
print(numero)
'''
#Apenas usando 'random.random' o computador escolhe um número aleatório entre 0 e 1

#Agora para escolher um número entre um  conjunto de números específico:
import random
numero=random.randint(1,500,)
print(numero)

