#Primeira e última ocorrência de uma string
nome = str(input('Digite seu nome: ')).upper().strip()
print('A letra A se repete {} vezes'.format(nome.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(nome.find('A')+1))
print('A letra A aparece pela última vez na posição {}'.format(nome.rfind('A')+1))

#Usa-se o upper para ajudar na escrita do código, usando a lógica que voce já havia entendido.
#O strip serve para que na contagem de letras não seja levado em consideração os espaços, caso surja.
#O +1 serve para que a contagem fique mais fácil para as pessoas, levando em consideração que a contagem inicia no 0.