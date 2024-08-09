#Escreva um código que leia o nome da cidade e que indique 'verdeiro' apenas para cidades que começam com "Santo"
cid = input('Em que cidade você nasceu? ').strip()
cidm = cid.upper()
print('Seu nome tem Santo? {}'.format(cidm[:5] == 'SANTO'))
