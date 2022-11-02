"""
. Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. unija, koja prihvata dve liste (bilo kog tipa podataka), a ima povratnu vrednost koja je lista 
sastavljena od svih elemenata obe liste bez ponavljanja.
Primer: unija([5, 4, "1", "8", 3, 7], [1, 9, "1"]) = [5, 4, "1", "8", 3, 7, 9, 1]
a. suma, koja formira novu listu tako što nalazi sumu svih elemenata u podlistama. Zabranjeno je 
korišćenje petlji i funkcije sum.
Primer: suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) = [6, 15, 24]


"""

from functools import reduce


def unija(a:list[object],b:list[object])->list[object]:
    return list(dict.fromkeys(a+b))

print(unija([5, 4, "1", "8", 3, 7], [1, 9, "1"]))

def suma(a:list[list[int]])->list[int]:
    return list(map(lambda x: reduce(lambda y,z: y+z,x) ,a))

print(suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))