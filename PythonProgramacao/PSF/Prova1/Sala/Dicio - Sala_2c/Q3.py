import json
#   Entrada para JSON
JSON = '{"valor":32.0,"unidade":"graus fahrenheit"}'

#   Convertendo para dicionário
dicionario = json.loads(JSON)

#   Convertendo temperaturas
celsius = (dicionario['valor'] - 32) * 5/9

#   Relacionando valores
dicionario['valor'] = celsius
dicionario['unidade'] = 'graus celsius'

print(dicionario)
