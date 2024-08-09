fahr = float(input())
conversao = (fahr - 32) * (5/9)

dicioF = {
    'valor' : fahr,
    'unidade' :'graus fahrenheit'
}
dicioC = {
    'valor' : conversao,
    'unidade' : 'graus celsius'
}
print(dicioF)
print(dicioC)
print(conversao)
print('graus celsius')
