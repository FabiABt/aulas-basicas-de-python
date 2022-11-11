#Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média aritmética das notas. 
# O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado (média superior ou igual a 5,0)
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
media = (n1+n2)/2
if media >= 5.0: 
    print("Parabéns você foi aprovado!")
else:
    print("Infelizmente você não foi aprovado!")