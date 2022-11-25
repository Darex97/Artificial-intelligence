from ast import Num
from itertools import zip_longest
from numbers import Number

"""
. Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. numlista, koja iz liste koja može da sadrži elemente različitog tipa izdvaja samo numeričke 
vrednosti
Primer: numlista(["Prvi", "Drugi", 2, 4, [3, 5]]) = [2, 4]
spojidict, koja 2 liste obejkata objedinjuje u listu sa elementima tipa dictionary. Dužina liste je 
dimenzija duže od dve ulazne liste. N-ti dictionary element rezultujuće kolekcije čine n-ti objekti
iz obe ulazne liste, gde se na prvoj poziciji nalazi element prve liste uparen sa ključem 'prvi', a 
na drugoj poziciji element druge liste uparen sa ključem 'drugi'. Kraću ulaznu listu dopuniti sa 
' - ', dok dužine obe liste ne budu iste. Zabranjeno je korišćenje petlji.
Primer: spojidict([1, 7, 2, 4], [2, 5, 2]) = [{'prvi': 1, 'drugi': 2}, {'prvi': 7, 
'drugi': 5}, {'prvi': 2, 'drugi': 2}, {'prvi': 4, 'drugi': '-'}]


"""

lista = ["Prvi","Drugi",2,5,[3,5]]

def numlista(lista:list)->list[int]:
    return list(filter(lambda x: type(x) == int,lista))

def spojidict(a:list,b:list)->list[dict[str,object]]:
    return list(map(lambda x: dict({'prvi' : x[0], 'drugi' : x[1]}), list(zip_longest(a,b, fillvalue='-'))))



print(spojidict([1, 7, 2, 4], [2, 5, 2]))
#print(numlista(lista))