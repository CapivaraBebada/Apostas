import math
graus = int(input())
rad =  ((math.pi) / (180)) * graus
seno = math.sin(rad)
formula = 100 * ((rad / seno) - 1)
print('{:.1f}%'.format(formula))

