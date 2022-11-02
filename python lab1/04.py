
from ast import Not
from functools import reduce
from itertools import accumulate
"""
4. Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. zbir, koja kreira novu listu čiji su elementi zbirovi susednih elementa liste.
Primer: zbir([1, 2, 3, 4, 5]) = [3, 5, 7, 9]
b. suma, koja vraća sumu svih elemenata u listi brojeva i svim njenim podlistama. Zabranjeno je 
korišćenje petlji i funkcije sum.
Primer: suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) = 45



"""

def upari(a:list):
    return [(a[i],a[i+1]) for i in range(0,len(a)-1)]

def zbir(a:list)->list[int]:
    return list(map(lambda x: x[0]+x[1] ,upari(a)))

#print(zbir([1, 2, 3, 4, 5]))
"""
def saberi(a:list[int]):
    return reduce(lambda x,y: x+y,a)
"""
def suma(a:list[list[int]])->int:
    return reduce(lambda x,y: x+y if type(x) == int and type(y) == int else reduce (lambda z,b: z+b,x) + y if type(y)==int else x + reduce(lambda z,b: z+b,y) if type(x)==int else reduce(lambda z,b: z+b,x)+reduce(lambda z,b: z+b,y),a)

#print(saberi([1,2,3]))  
print(suma([[1, 2, 3],[4, 5, 6],[7, 8, 9]]))