"""
16. Korišdenjem programskog jezika Python, napisati funkciju broj, koja na osnovu heksadekadnog
broja koji predstavlja boju na ulazu u formatu #RGB, određuje integer reprezentaciju tog broja, koja
se dobija slededim obrascem: (R * 65536) + (G * 256) + B. Zabranjeno je korišdenje petlji (osim u
comprehension sintaksi).
Napomena: Broj N je mogude prevesti iz baze B u bazu 10 korišdenjem funkcije int(N, B)
Primer: broj("#FA0EA0") = 16387744
"""
from functools import reduce


def broj(A:hex)->int:
    return reduce(lambda p,q: p+q,list(map(lambda x: int(x[1],16)*65536 if x[0] == 0 else int(x[1],16)*256 if x[0]==1 else int(x[1],16) ,enumerate([(A[i]+A[i+1]) for i in range(1,len(A)-1,2)] ))))


print("----------------------------------------------------")
print(broj("#FA0EA0"))





#250 14 160


