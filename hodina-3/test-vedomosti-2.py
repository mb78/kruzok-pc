#!/bin/env python3

# vylepsenie: vyhodnotenie 3 otazok pomocou funkcie

# otvor ('open') subor 'matematika.test' a spristupni ho pomocou premennej 'subor'
subor=open('matematika.test')

def spracuj_otazku():
    print('------------------------------------------')
    # prvy riadok: zadanie alebo otazka s 3 moznostami
    otazka=subor.readline()
    # moznosti su oznacene a, b, c
    moznost_a=subor.readline()
    moznost_b=subor.readline()
    moznost_c=subor.readline()

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
