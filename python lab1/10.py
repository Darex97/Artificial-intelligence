"""
. Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. izbroj, koja određuje broj elemenata liste, gde svaki element može da bude podlista ili broj.
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi).
Primer: izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]) = 13
b. stepen, koja svaki par dva broja u ulaznoj listi (x, y), transformiše u xy
.
Primer: stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]) = [1, 25, 64, 6, 1, 216, 9, 512]
"""

from functools import reduce
from itertools import pairwise


def izbroj(a:list)->int:
    return reduce(lambda acc,x: acc+1 if type(x)==int else acc+izbroj(x),a,0)

print(izbroj([1, [1, 3, [2, 4, 5, [5, 5], 4]], [2, 4], 4, 6]))


def stepen(a:list)->list[int]:
    return list(map(lambda x: reduce(lambda y,z: y**z,x),pairwise(a)))
print(stepen([1, 5, 2, 6, 1, 6, 3, 2, 9]))