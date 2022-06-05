#sorteando uma orddem na lista 
import random
p1 = input(" Digite o nome da 1 pessoa: ")
p2 = input(" Digite o nome da 2 pessoa: ")
p3 = input(" Digite o nome da 3 pessoa: ")
p4 = input(" Digite o nome da 4 pessoa: ")
lista = [p1, p2, p3, p4]
escolhido = random.choice(lista)
print("O aluno sorteado e: {}".format(escolhido))
#ou 
print(" O aluno sorteados e: {}".format(random.choice(lista)))