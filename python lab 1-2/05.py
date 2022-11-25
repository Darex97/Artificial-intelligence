from functools import reduce
"""
Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. brojel, koja broji koliko elemenata ima svaka podlista liste koja joj je prosleđena. Ukoliko 
elemenat liste nije podlista funkcija vraća -1.
Primer: brojel([1, 2], [3, 4, 5], 'el', ['1', 1]) = [2, 3, -1, 2]
b. proizvod, koja računa proizvod liste podlisti (A) i liste brojeva (B). Smatrati da je broj podlisti u 
listi A jednak dužini liste B. Funkcija vraća listu koja ima onoliko elemenata koliko je dužina 
ulaznih listi. N-ti element izlatne liste predstavlja sumu svih elemenata N-te podliste liste A koji u 
prethodno pomnoženi N-tim elementom u liste B. Zabranjeno je korišćenje petlji i funkcije sum.
Primer: proizvod([[1,2,3],[4,5,6],[7,8,9]], [1,2,3]) = [6, 30, 72]



"""

def brojel(a:list)->list[int]:
    return list(map(lambda x: len(x) if not type(x)== int else -1,a))

print( brojel([[1, 2], [3, 4, 5], 'el', ['1', 1],1,[2,'h']]))

def proizvod(a:list[list[int]], b:list[int])->list[int]: 
    return  list(map(lambda x: reduce(lambda y,z: y+z,x[0])* x[1],zip(a,b)))

print(proizvod([[1,2,3],[4,5,6],[7,8,9]], [1,2,3]))
