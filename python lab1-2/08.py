"""
Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. izmeni, koja svaki n-ti element liste zamenjuje brojem koji predstavlja sumu svih elemenata 
originalne liste, od prvog, do n-tog elementa.
Primer: izmeni([1, 2, 4, 7, 9]) = [1, 3, 7, 14, 23]

b. izracunaj, koja u listi koja može da se sastoji od brojeva i podlisti, na n-tom mestu u rezultujućem 
nizu upisuje broj sa n-te pozicije iz ulaznog niza, a ukoliko se radi o podlisti, zamenjuje je 
proizvodom svih brojeva u podlisti.
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi).
Primer: izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]) = [1, 5, 15, 8, 2, 18]

"""

from functools import reduce
from itertools import accumulate
import operator


def izmeni(lista):
    return list(accumulate(lista,operator.add))

print(izmeni([1, 2, 4, 7, 9]))

def izracunaj(a:list[int or list[int]])->list[int]:
    return list(map(lambda x: x if type(x)==int else reduce(lambda y,z: y*z,x),a))

print(izracunaj([1, 5, [1, 5, 3], [4, 2], 2, [6, 3]]))