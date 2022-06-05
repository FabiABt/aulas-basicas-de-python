# Um professor quer sortear um dos seus quatro alunmos para apagar o quadro. Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
import random
p1 = str(input(" Digite o nome da 1 pessoa: ")),
p2 = str(input(" Digite o nome da 2 pessoa: ")),
p3 = str(input(" Digite o nome da 3 pessoa: ")),
p4 = str(input(" Digite o nome da 4 pessoa: ")),
lista = [p1, p2, p3, p4]
escolhido = random.choise(lista)
print("O aluno sorteado e {}".format(escolhido))
# tem essa outa forma 
print(" O aluno sorteado e: {}".format(random.choice(lista(p1,p4))))