tensao_string = input().split()
corrente_string = input().split()
# Convertee
tensao_float = [float(i) for i in tensao_string]
corrente_float = [float(i) for i in corrente_string]
# media
if len(tensao_string) == len(corrente_string):
    resistencia = sum([tensao_float[i] / corrente_float[i] for i in range(len(tensao_string))])
    media = resistencia / len(tensao_string)
    print(f'Resitência média: {media:.2f} ohms')
else:
    print('A quantidade de dados para Tensão e Corrente elétrica são diferentes!')
