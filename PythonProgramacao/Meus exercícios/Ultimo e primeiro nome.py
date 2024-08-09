# Colocar o último nome da pessoa no início e o último no início
# EX: Marcos Antônio de Souza = Souza, Marcos

nome = str(input('Digite seu nome: '))
lnom = nome.split()
rnom = nome.split()
print('Seu nome ficou: {} {}'.format(rnom[len(rnom)-1], lnom[0]))
