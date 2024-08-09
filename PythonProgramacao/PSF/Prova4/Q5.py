from math import exp
from math import factorial

def erroexp(x, n):

#   Calculo direto
    funcao_direta = exp(x)

#   Usando a questao 3
    conta = (1 + (x / n)) ** n

#   Usando a questao 4
    soma = 0
    for i in range(n):
        divisao = (x ** i) / factorial(i)
        soma += divisao

#   Calculando erro
    erro1 = (conta - funcao_direta) / funcao_direta * 100
    erro2 = (soma - funcao_direta) / funcao_direta * 100

    return soma, conta, erro1, erro2
soma, conta, erro1, erro2 = erroexp(5,6)
print(f"exp(5.0) = {exp(5.0):.2f}")
print(f"exp1(5.0, 6) = {erro1:.3f} - Erro: {erro1:.3f} %")
print(f"exp2(5.0, 6) = {erro2:.3f} - Erro: {erro2:.3f} %")
