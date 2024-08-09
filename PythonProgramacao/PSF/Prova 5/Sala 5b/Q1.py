import numpy as np

numero = int(input())
vetor = np.array([1,2,3,4])
print(vetor)
vetor = np.append(vetor, numero)
print(vetor)
print(vetor[4])