import json
far = 32
#   Conversao de unidade
celsius = (far - 32) * (5/9)
#   Criando dicionário
dicio_F = {
    'valor' : far,
    'unidade' : 'graus fahrenheit'
}
dicio_C = {
    'valor' : celsius,
    'unidade' : 'graus celsius'
}
#   Convertendo para JSON
json_F = json.dumps(dicio_F)
json_C = json.dumps(dicio_C)

temperatura = {'valor' : far, 'unidade' : unidade}