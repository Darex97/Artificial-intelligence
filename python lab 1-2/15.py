"""

Korišćenjem programskog jezika Python, napisati sledeće funkcije:
a. izdvoji, koja iz zadate liste čiji su elementi liste, izdvaja n-ti element i formira rezultujuću listu, pri 
čemu je n=0 za prvu podlistu i uvećava se sukcesivno za 1. Ukoliko ne postoji n-ti element u listi 
vraća se 0.
Primer: izdvoji([5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]) = [5, 9, 0, 12]
b. promeni, koja u listi brojeva, brojeve veće ili jednake broju x, koji se prosleđuje kao argument, 
umanjuje za x, dok brojeve manje od x uvećava za x
Primer: promeni([7, 1, 3, 5, 6, 2], 3) = [4, 4, 6, 2, 3, 5]
"""
from operator import index


def izdvoji(a:list[list[int]])->list[int]:
    return list(map(lambda x: x[a.index(x)] if len(x)>a.index(x) else 0 ,a))

print(izdvoji([[5, 4, 4], [1, 9, 1], [5, 6], [4, 6, 10, 12]]))

def promeni(a:list[int],b:int)->list[int]:
    return list(map(lambda x: x-b if x>=b else x+b,a))
print(promeni([7, 1, 3, 5, 6, 2], 3))