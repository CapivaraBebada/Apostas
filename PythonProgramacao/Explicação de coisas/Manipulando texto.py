# Toda frase escrita é formada por letras e cada letra ocupa um espaço, tal espço é igual para todas elas.
# A contagem de letras (ou espaços) inicia do zero até a última casa a ser usada, seja letra ou não.
# O python entende esse seguimento de espaços como uma lista e para se referir a lista no python, usa-se os colchete '[]'.
# OBS: O python consegue disernir entre letras maiúsculas e minúsculas.

# Exemplo: frase('O abacaxi está estragado')
# Temos 24 espaços, e se quiséssemos escolher um espaço específico seria: frase[3].
# Nesse caso o a letra que está sendo ocupada na posição 3 é 'b'.

# O que acabou de ser feito foi o fateamento. Uma outra forma de fatear é:
# Exemplo: frase('O abacaxi está estragado')
# Frase[0:4] - Isso significa que o python selecionará do 0 até o 3 (isso mesmo)!

# Outro caso que pode ocorrer é selecionar uma lista de espaços, mas desta vez, pulando espaços de forma padronizada.
# Os que foram pulados não serão levados em consideração.
# Exemplo: frase('O abacaxi está estragado')
# Frase[0:21:2] - Significa que será selecionado espaços do 0 até o 20 pulando de 2 em 2.

# Se ocorrer de frase[:7] - Então a contagem inicia do início (zero) e termina no 6.
# Se ocorrer de frase[4:] - Então iniciará do 4 até a última casa.
# Se ocorrer de frase[9::3] - Inicia do 9 e vai até o final pulando de 3 em 3.

    # Análise se string
# Uma forma de analisar é saber o comprimento da frase, para isso usa-se o "len(frase)"
# A quantidade de lens é a quantidade de caracteres da frase

# frase.count('t') - Sua ideia é contar quantas vezes a letra dentro do parênteses aparece na frase.
# frase.count('o',0,19) - Ele realiza o fateamento e a contagem ao mesmo tempo. Neste caso, a contagem da letra 'o' será
# feita entre o zero e o 19.
# frase.find('aba') - Te indicará onde começa a sequecência específica de "aba".
# frase.find(tor) - Perceba que não há esta função na frase, então o sistema lhe retornará "-1" como sinal de que não
# foi encontrado

# 'está'infrase - retornará "true", pois existe essa sequência específica de letras na frase "O abacaxi está estragado".
# 'cabo'infrase - retornará false

    # Transformação
# frase.replace('abacaxi, cabo') - Onde tiver "abacaxi" será substituído por "cabo".
# frase.upper() - Determina que todas as letras ficarão maiúsculas.
# frase.lower() - Determina que todas as letras ficarão minúsculas.
# frase.capitalize() - Apenas a primeira posição será maiúscula.
# frase.title() - Cada início de palavra ficará maiúscula.
# frase.strip() - Remove os espaços inúteis no início e no final da frase.
# frase.rstrip() - Remove apenas os espaços inúteis à direita (right) da frase.
# frase.lstrip() - Remove apenas os espaços inúteis à esquerda (left) da frase.

   #Divisão
# frase.split() - Cria uma divisão a cada espaço; a contagem inicia-se ao início de cada palavra (sempre do zero).

   #Junção
# '-'.join(frase) - Em cada espaço será adicionado um hífen entre as palavras. Porém, qualquer coisa que quiser colocar
#entre as aspas ficará entre as palavras.