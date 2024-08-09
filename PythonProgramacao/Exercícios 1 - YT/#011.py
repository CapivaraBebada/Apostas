#Digite um valor em metros e converta-o para as demais unidades de medida

a=float(input('Digite uma metragem: '))
km=(a/1000)
he=(a/100)
de=(a/10)
dec=(a*10)
cm=(a*100)
mm=(a*1000)
print("As devidas unidades de medida para esse valor são:")
print('{} km\n{} hm\n{} dam\n{} m\n{} dm\n{} cm\n{} mm\n'.format(km,he,de,a,dec,cm,mm))