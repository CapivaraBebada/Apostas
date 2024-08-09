'''
U = R * I
U: Tensao; R: Resistencia; I: Corrente
R = U / I
'''
# Recebe as entradas
tensao = input().split()
corrente = input().split()
# Converte para float
tensao_float = [ float(i) for i in tensao ]
corrente_float = [ float(i) for i in corrente ]
if len(tensao) != len(corrente):
    print('A quantidade de dados para Tensão e Corrente elétrica são diferentes!')
else:
    resistencia = sum([ tensao_float[i] / corrente_float[i] for i in range(len(tensao)) ]) / len(tensao)
    print(f'Resistencia média: {resistencia:.2f} ohms')
