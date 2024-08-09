frase='O abacaxi está estragado!'
print(frase[24])
#Fateando:
print(frase[3:19])
print(frase[:15])
print(frase[12:])
print(frase[1:20:2])
print(frase.count('a'))
print(frase.upper())
print(frase.upper().count('O'))
print(frase.lower())
print(frase.lower().count('t'))
print(frase.replace('abacaxi', 'maçã'))
print(frase.split())

#Atenção aqui embaixo:
outra=('O abacaxi está estragado')
dividido=outra.split()
print(dividido[3][3])
