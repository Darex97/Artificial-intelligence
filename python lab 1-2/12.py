"""
Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. presek, koja prihvata dve liste (bilo kog tipa podataka), a ima povratnu vrednost koja je lista 
sastavljena od svih elemenata koji se nalaze u obe liste.
Primer: presek([5, 4, "1", "8", 3, 7], [1, 9, "1"]) = [1, "1"]
a. izracunaj, koja u listi koja se sastoji od brojeva i podlisti, menja svaki broj njegovim kvadratom, 
dok listu zamenjuje zbirom kvadrata brojeva koji je čine. 
Zabranjeno je korišćenje petlji (osim u comprehension sintaksi).
Primer: izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]) = [4, 16, 14, 20, 4, 106]


"""



from functools import reduce


def presek(a:list[object],b:list[object])->list[object]:
    return list(filter(lambda x: x in b ,a))
    

print(presek([1,5, 4, "1", "8", 3, 7], [1, 9, "1"]))

def izracunaj(a:list[int or list[int]])->list[int]:
    return list(map(lambda x: x**2 if type(x)==int else reduce(lambda z,y: z+y,map(lambda t: t**2,x)),a))

print(izracunaj([2, 4, [1, 2, 3], [4, 2], 2, [9, 5]]))