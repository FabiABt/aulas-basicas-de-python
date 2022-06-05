# um professor deseja sortear a ordem de apresentacao dos alunos 
from random import shuffle 
p1 = input(" Digite o nome do primeiro aluno: ")
p2 = input(" Digite o nome do segundo aluno: ")
p3 = input(" Digite o nome do terceiro aluno: ")
p4 = input(" Digite o nome do quarto aluno: ")
lista = [p1, p2, p3, p4]
shuffle(lista)
print("A ordem de apresentacao sera: ")
print(lista)