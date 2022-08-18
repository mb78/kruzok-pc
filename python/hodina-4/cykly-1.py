#!/bin/env python3

# Ako vypisat cisla 1,2,3, jedno na kazdy riadok ?
# Na zaciatok
print(1)
print(2)
print(3)

# Alebo pomocou cyklu 'for'
# v preklade to znamena:
# - prirad premennej 'i' hodnotu 1 z funkcie range(1,4) a vykonaj print(i)
# - zober dalsiu hodnotu, cize 2, je mensia ako 4 ? ano, prirad i=2, zavolaj print(i)
# - dalsia hodnota je 3, takisto
# - dalsia hodnota je 4, ta uz je rovna druhemu parametru (argumentu) funkcie range(1,4), ukonci cyklus
for i in range(1,4):
    print(i)

# range(1,4) funkcia umozni cyklu for zopakovat print(i) 3 krat, pre hodnotu v druhom parametri sa uz nezavola
