"""
Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. operacija, koja listu tuple vrednosti transformiše u listu brojeva, koji se dobijaju primenom 
operacije prosleđene putem argumenta.
Primer: operacija([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y) = [11, 6, 5]
b. objedini, koja od liste tuple objekata kreira dictionary. Prvi element svakog tuple objekta postaje 
ključ rečnika, dok sve ostale vrednosti postaju vrednost (lista vrednosti).
Ukoliko tuple podatak ima manje od 2 vrednosti, na mesto vrednosti postaviti None.
Ukoliko ključ već postoji u rečniku, prepisati njegovu vrednost novom.
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi).
Primer: objedini([(1), (3, 4, 5), (7), (1, 4, 5), (6, 2, 1, 3)]) = { 1: [4, 5], 3: [4, 
5], 7: None, 6: [2, 1, 3] }


"""

from functools import reduce


def operacija(lista, op, neutral):
    return list(map(lambda x: reduce(op, x, neutral), lista))

print(operacija([(1, 4, 6), (2, 4), (4, 1)], lambda x, y: x + y, 0))



def objedini(A:list):
   return dict(reduce(lambda acc,el: acc | {str(el[0]): el[1:] if el[1:] else None}, A, dict()))

print(objedini([(1,), (3, 4, 5), (7,), (1, 4, 5), (6, 2, 1, 3)]))