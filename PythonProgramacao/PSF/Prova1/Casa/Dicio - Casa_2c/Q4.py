import json
fahr = float(input())
#   Conversão para celsius:
celsius = (fahr - 32) * (5/9)
#   Criando dicionario
dicioF = {
    'valor': fahr,
    'unidade': 'graus fahrenheit'
}
diciC = {
    'valor': celsius,
    'unidade': 'graus celsius'
}
#   Convertendo dicionário
json_dicioF = json.dumps(dicioF)
json_dicioC = json.dumps(diciC)
print(json_dicioF)
print(json_dicioC)