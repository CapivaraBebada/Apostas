#Sortear 4 pessoas em ordem
import random
a=input('Pessoa1: ')
b=input('Pessoa2: ')
c=input('Pessoa3: ')
d=input('Pessoa4: ')
e=[a,b,c,d]
random.shuffle(e)
print('A ordem das pessoas será: {}'.format(e))

#'Shuffle' significa 'embaralhar'