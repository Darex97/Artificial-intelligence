"""
Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. prosek, koja za svaki element prosleđene liste, koja se sastoji isključivo od podlisti, vraća 
aritmetičku sredinu svih njenih vrednosti.
Primer: prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]) = [3.25, 4.75, 4.0, 
5.0]
b. zamena, koja u listi brojeva, brojeve manje od broja x, koji se prosleđuje kao argument, 
zamenjuje zbirom svih vrednosti ulazne liste, koje imaju indeks veći od indeksa broja koji se 
obrađuje.
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi).
Primer: zamena([1, 7, 5, 4, 9, 1, 2, 7], 5) = [35, 7, 5, 19, 9, 9, 7, 7]


"""

from functools import reduce
import operator


def prosek(a:list[list[int]])->list[float]:
    return list(map(lambda x: reduce(lambda y,z: y+z,x)/len(x),a))

print(prosek([[1, 4, 6, 2], [4, 6, 2, 7], [3, 5], [5, 6, 2, 7]]))

def zamena(a:list[int],b:int)->list[int]:
    return list(map(lambda x: x if x>=b else reduce(lambda r,t: r+t,a[operator.index(x):]),a))

print(zamena([1, 7, 5, 4, 9, 1, 2, 7], 5))


