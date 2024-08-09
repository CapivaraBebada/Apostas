# Velocidade de um carro e multa
vel = float(input('Velocidade do carro: '))
max = 80
M = (vel-80)*7

if vel < max:
    print('Não há multa, pois sua velocidade foi de \033[42:30m{:.2f}km/h\033[m'. format(vel))
elif vel > max:
    print('Sua velocidade foi de \033[41:30m{}km/h\033[m e sua multa de {:.2f} reais'.format(vel, M))
else:
    print('Sua velocidade foi de \033[43:30m{}km/h\033[m. No limite da via!'.format(vel))
