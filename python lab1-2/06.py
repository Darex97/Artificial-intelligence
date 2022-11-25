"""
Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. razlika, koja prihvata dve liste (bilo kog tipa podataka), a ima povratnu vrednost koja je lista 
sastavljena od svih elemenata iz prve liste, koji se ne nalaze u drugoj listi.
Primer: razlika([1, 4, 6, "2", "6"], [4, 5, "2"]) = [1, 6, "6"]
b. objedini, koja 2 liste brojeva objedinjuje u jednu listu koja se sastoji od parova brojeva (tuple). 
Dužina liste treba da je dimenzija duže od dve ulazne liste. N-ti tuple podatak rezultujuće 
kolekcije čine n-ti brojevi iz obe ulazne liste, gde na prvoj poziciji treba da se nađe manji, a na 
drugoj veći broj iz obe liste.
Kraću ulaznu listu dopuniti sa kraja brojem 0, dok dužine obe liste ne budu iste.
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi).
Primer: objedini([1, 7, 2, 4, 5], [2, 5, 2]) = [(1, 2), (5, 7), (2, 2), (0, 4), (0, 5)]



"""

from itertools import zip_longest


def razlika(a:list[object],b:list[object])->list[object]:
    return list(filter(lambda x: x not in b,a))

print(razlika([1, 4, 6, "2", "6"], [4, 5, "2"]))

def objedini(a:list[object],b:list[object])->list[object]:
    return list(map(lambda x: (x[0],x[1]) if x[0]< x[1] else (x[1],x[0]),zip_longest(a,b,fillvalue=0)))

print(objedini([1, 7, 2, 4, 5], [2, 5, 2]))