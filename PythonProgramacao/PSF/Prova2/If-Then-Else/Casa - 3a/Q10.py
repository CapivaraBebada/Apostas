renda = float(input())

if renda <= 1903.98:
    print(f'Renda: R$ {renda:.2f}')
    print('Isento de pagamento.')
elif 1903.98 < renda <= 2826.66:
    segunda_faixa = (renda - 1903.98) * 0.075
    print(f'Renda: R$ {renda:.2f}')
    print(f'Imposto a pagar: R$ {segunda_faixa:.2f}')
elif 2826.66 < renda <= 3751.06:
    segunda_faixa = (2826.66 - 1903.98) * 0.075
    terceira_faixa = ( (renda - 2826.66) * 0.15) + segunda_faixa
    print(f'Renda: R$ {renda:.2f}')
    print(f'Imposto a pagar: R$ {terceira_faixa:.2f}')
elif 3751.06 < renda <= 4664.48:
    segunda_faixa = (2826.66 - 1903.98) * 0.075
    terceira_faixa = ((3751.06 - 2826.66) * 0.15) + segunda_faixa
    quarta_faixa = ( (renda - 3751.06) * 0.225 ) + terceira_faixa
    print(f'Renda: R$ {renda:.2f}')
    print(f'Imposto a pagar: R$ {quarta_faixa:.2f}')
elif renda > 4664.48:
    segunda_faixa = (2826.66 - 1903.98) * 0.075
    terceira_faixa = ((3751.06 - 2826.66) * 0.15) + segunda_faixa
    quarta_faixa = ((4664.48 - 3751.06) * 0.225) + terceira_faixa
    quinta_faixa = ( (renda - 4664.48) * 0.275) + quarta_faixa
    print(f'Renda: R$ {renda:.2f}')
    print(f'Imposto a pagar: R$ {quinta_faixa:.2f}')
