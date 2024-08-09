renda = float(input())
imposto = (renda - 1903.98) * 0.20

if renda < 1903.98:
    print(f'Renda: R$ {renda:.2f}')
    print('Isento de pagameto')
else:
    print(f'Renda: R$ {renda:.2f}')
    print(f'Imposto a pagar: R$ {imposto:.2f}')
