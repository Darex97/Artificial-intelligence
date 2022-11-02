
"""
 Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. izmeni, koja kreira novu listu tako da elemente na parnim pozicijama uvećava za jedan, dok 
elemente na neparnim pozicijama umanjuje za 1.
Primer: izmeni([8, 5, 3, 1, 1]) = [9, 4, 4, 0, 0]
b. skupi, koja kreira novu listu tako da svaka dva susedna elementa liste ciji su elementi iskljucivo 
podliste zamenjuje podlistom koja sadrži zbir elemeata na odgovarajućim pozicijama. Zabranjeno 
je korišćenje petlji.
Primer: skupi([[1, 3, 5],[2, 4, 6],[1, 2]]) = [[3, 7, 11],[3, 6, 6]]
"""

from itertools import pairwise, starmap
from operator import index


def izmeni(a:list[int])->list[int]:
    return list(map(lambda x: x+1 if a.index(x)%2==0 else x-1,a))

print(izmeni([8, 5, 3, 1, 1]))

def skupi(a:list[list[int]])->list[list[int]]:
    return list(map(lambda x: list(map(lambda z,y: z + y ,x[0],x[1])),pairwise(a)))

print(skupi([[1, 3, 5],[2, 4, 6],[1, 2]]))