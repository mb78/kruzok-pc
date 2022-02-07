#!/bin/env python3

# vylepsenie: odstranenie prazdnych riadkov

# nacitanie modulu (dalsich funkcii python-u) "sys"
import sys

SUBOR='matematika.test'
if (len(sys.argv)>1):
    SUBOR=sys.argv[1]

# otvor ('open') subor 'matematika.test' a spristupni ho pomocou premennej 'subor'
subor=open(SUBOR)

def spracuj_otazku():
    print('------------------------------------------')
    # prvy riadok: zadanie alebo otazka s 3 moznostami
    otazka=subor.readline().strip()
    # moznosti su oznacene a, b, c
    moznost_a=subor.readline().strip()
    moznost_b=subor.readline().strip()
    moznost_c=subor.readline().strip()

    # subor po moznostiach obsahuje riadok so spravnou odpovedou, tiez a, b alebo c
    spravna_odpoved=subor.readline().strip()

    # vypisanie otazky zo suboru
    print(otazka)
    # a moznosti
    print('a)',moznost_a)
    print('b)',moznost_b)
    print('c)',moznost_c)

    # nacitaj odpoved
    odpoved=input('Zadaj odpoved (a, b alebo c):')

    # kontrola odpovede
    if (odpoved==spravna_odpoved):
        print('Spravne !')
    else:
        print('Nespravne ! odpoved',spravna_odpoved+')','bol spravna')

spracuj_otazku()
spracuj_otazku()
spracuj_otazku()
