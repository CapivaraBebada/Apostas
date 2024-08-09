# Primeiro e último nome
nome = str(input('Digite seu nome completo: ')).strip()
nom = nome.split()
print('Seu primeiro nome é {}'.format(nom[0]))
print('Seu último nome é {}'.format(nom[len(nom)-1]))

# Atenção na forma que foi usada a função "split".
# Não entendi o -1, mas apenas aceite que ele lê o último nome!