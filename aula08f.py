#sorteando uma orddem na lista 
from random import shuffle 
p1 = input(" Digite o nome da 1 pessoa: ")
p2 = input(" Digite o nome da 2 pessoa: ")
p3 = input(" Digite o nome da 3 pessoa: ")
p4 = input(" Digite o nome da 4 pessoa: ")
lista = [p1, p2, p3, p4]
shuffle(lista)
print("A ordem de apresentacao sera: ")
print(lista)