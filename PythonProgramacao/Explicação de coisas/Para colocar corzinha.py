# Exemplo dos códigos que provavelmente serão usados:
#Apenas Sublinhado
print('\033[4mO pé de macaxeira foi roubado!\033[m')
#Apenas Backgound preto
print('\033[40mO pé de macaxeira foi roubado!\033[m')
#Background preto sublinhado
print('\033[40:4mO pé de macaxeira foi roubado!\033[m')
#Apenas backgound vermelho com letra preta
print('\033[41:30mO pé de macaxeira foi roubado!\033[m')
#Apenas backgound verde com letra preta
print('\033[42:30mO pé de macaxeira foi roubado!\033[m')
#Apenas backgound amarelo com letra preta
print('\033[43:30mO pé de macaxeira foi roubado!\033[m')



#   Padrão ANSI: padrão de normalização internacional.
#   ANSI para cores: \033[m
#   Entre o colchete e o "m" vem o código da cor, o "m" indica o término do código.
#   Para indicar o código, primeiramente deverá indicar qual o estilo "style", texto "text" e cor de fundo "background"
#   Tudo isso acima deverá ser escrito entre o colchete e o "m".
#   EX: \033[0:33:44m

#   Para style:
#       0: none (terminal)
#       1: bold (letra um pouco mais estreita)
#       4: underline
#       7: negative


#   Para Text:
#       30: white
#       31: red
#       32: green
#       33: yellow
#       34: blue
#       35: purple
#       36: light blue
#       37: gray

#   Para Background
#       40: white
#       41: red
#       42: green
#       43: yellow
#       44: blue
#       45: purple
#       46: light blue
#       47: gray


# Exemplo dos códigos que provavelmente serão usados:
print('\033[4mO pé de macaxeira foi roubado!\033[m')         #Apenas backgound preto
print('\033[40mO pé de macaxeira foi roubado!\033[m')        #Apenas backgound preto
print('\033[40:4mO pé de macaxeira foi roubado!\033[m')      #Apenas backgound preto
print('\033[41:30mO pé de macaxeira foi roubado!\033[m')     #Apenas backgound vermelho com letra preta
print('\033[42:30mO pé de macaxeira foi roubado!\033[m')     #Apenas backgound verde
print('\033[43:30mO pé de macaxeira foi roubado!\033[m')     #Apenas backgound preto








