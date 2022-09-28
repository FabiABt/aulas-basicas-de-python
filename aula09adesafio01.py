# crie um programa que leia o nome completo de uma pessoa e mostre:
# a) o nome com trodas as letras maiusculas
# b) o nome com todas as letras em caixa baixa 
# c) quantas letras tem o nome sem considerar os pepaços
# d) quantas letras tem o primeiro nome 
nome = str(input(" Digite seu nome completo: "))
print("nome : {}".format(nome))
#a
print(nome.upper())
#b
print(nome.lower())
#c
print(len(nome.replace(" ", "")))
print(len(nome.split()[0]))