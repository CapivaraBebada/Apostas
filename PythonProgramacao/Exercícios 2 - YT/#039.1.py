    # É o #039 só que um pouco diferente

from datetime import date
nas = int(input('Qual a sua data de nascimento? '))
atual = date.today().year
anos = atual - nas
servir = nas + 18
if anos < 18:
    print('Você nasceu em {}, tem {} anos e deverá servir no ano de {}'.format(nas, anos, servir))
elif anos > 18:
    print('Você nasceu em {}, tem {} anos e deveria ter servido no ano de {}'.format(nas, anos, servir))
else:
    print('Você nasceu em {}, tem {} anos e deve se alistar ainda este ano'.format(nas, anos))
