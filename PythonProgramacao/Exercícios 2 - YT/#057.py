resposta = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]

while resposta not in 'MmFf':
    print('Dados inválidos. Tente novamente!')
    resposta = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]
print('Sexo {} cadastrado com sucesso.'.format(resposta))
