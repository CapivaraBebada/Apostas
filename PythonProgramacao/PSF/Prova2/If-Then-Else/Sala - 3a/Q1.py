letra = input().upper()
dicionario = {
    'A' : 'T',
    'G' : 'C',
    'T' : 'A',
    'C' : 'G'
}
if letra in dicionario:
    print(dicionario[letra])
else:
    print('Base Nitrogenada Não Encontrada.')
