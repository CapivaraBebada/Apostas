import json
entrada_json = {"valor": 32.0, "unidade": "graus fahrenheit"}
#   Convertendo JSON para DICIONARIO:
dicionario = json.loads(entrada_json)
#   Conversao para Celcius
celsius = (dicionario['valor'] - 32) * (5/9)
#   Atribuíndo os valores
dicionario['valor'] = celsius
dicionario['unidade'] = 'graus celsius'
print('{}\n{}'.format(entrada_json, dicionario))
