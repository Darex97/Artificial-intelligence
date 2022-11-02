from itertools import zip_longest


"""
 Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. uredi, koja svaki od prvih n elemenata uvećava za definisanu vrednost a preostale umanjuje za 
definisanu vrednost. Funkciji se prosleđuje lista koja sadrži samo numeričke vrednosti i vrednost 
koja treba da se uvećava, odnosno umanjuje. Zabranjeno je korišćenje patlji.
Primer: uredi([1, 2, 3, 4, 5], 3, 1) = [2, 3, 4, 3, 4]
b. spoji, koja 2 liste brojeva objedinjuje u jednu listu koja se sastoji od tuple objekata koji imaju tri 
elementa. Prvi element rezultujuće kolekcije je element prve liste, drugi je element druge liste a 
treći je zbir elemenata. Dužina liste je dimenzija duže od dve ulazne liste. N-ti tuple podatak 
rezultujuće kolekcije čine n-ti brojevi iz obe ulazne liste, gde na prvoj poziciji treba da se nađe 
manji, a na drugoj veći broj iz obe liste.
Kraću ulaznu listu dopuniti sa kraja brojem 0, dok dužine obe liste ne budu iste. Zabranjeno je 
korišćenje petlji.
Primer: spoji([1, 7, 2, 4], [2, 5, 2]) = [(1, 2, 3), (5, 7, 12), (2, 2, 4), (4, 0, 4)]

"""

def uredi(lista:list[int],n:int,value:int)->list[int]:
   return [lista[i] + (value if i < n else - value) for i in range(0, len(lista))]

#print(uredi([1, 2, 3, 4, 5], 3, 1) )

def spoji(a:list[int],b:list[int])->list[tuple[int,int,int]]:
    return list(map(lambda x: (x[0] if x[0] < x[1] else x[1] , x[1] if x[1] > x[0] else x[0], x[0]+x[1]),zip_longest(a,b,fillvalue=0)))

print( spoji([1, 7, 2, 4], [2, 5, 2]))