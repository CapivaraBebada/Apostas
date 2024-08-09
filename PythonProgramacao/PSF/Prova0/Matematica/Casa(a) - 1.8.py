s = input()
hora, min, seg = map(int, s.split(':'))
total = hora*60 + min + seg/60

print(total)
