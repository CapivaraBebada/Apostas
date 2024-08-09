num = float(input())
hora = (num // 3600)
min = (num % 3600) // 60
seg = (num % 3600) % 60
print('{:.0f} h {:.0f} min {:.0f} s'.format(hora,min,seg))