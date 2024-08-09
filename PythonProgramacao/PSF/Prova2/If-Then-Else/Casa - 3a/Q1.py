letra = input().upper()
dicionario = {
    'T' : 'A',
    'A' : 'T',
    'C' : 'G',
    'G' : 'C'
}
if letra in dicionario:
    print(dicionario[letra])
else:
    print('Base Nitrogenada Não Encontrada.')