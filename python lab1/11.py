"""
Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. razlika, koja kreira novu listu čiji su elementi razlika susednih elementa liste.
Primer: razlika([8, 5, 3, 1, 1]) = [3, 2, 2, 0]
b. proizvod, koja vraća proizvod svih elemenata u listi brojeva i svim njenim podlistama. Zabranjeno 
je korišćenje petlji i funkcije prod.
Primer: proizvod([[1, 3, 5],[2, 4, 6],[1, 2, 3]]) = 4320

"""

from functools import reduce
from itertools import pairwise


def razlika(a:list[int])->list[int]:
    return list(map(lambda x: (x[0]-x[1]),pairwise(a)))

#print(razlika([8, 5, 3, 1, 1]))

def proizvod(a:list[list[int]])->int:
    return reduce(lambda x,y: x*y if type(x) == int and type(y)==int else proizvod(x)*proizvod(y) if not type(x) == int and not type(y)==int else x*proizvod(y) if type(x)== int and not type(y)==int else proizvod(x)*y,list(a))

#print(proizvod([1,2,3]))
print(proizvod([[1, 3, 5],[2, 4, 6],[1, 2, 3]]))