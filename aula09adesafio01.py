# crie um programa que leia o nome completo de uma pessoa e mostre:
# a) o nome com trodas as letras maiusculas
# b) o nome com todas as letras em caixa baixa 
# c) quantas letras tem o nome sem considerar os pepaços
# d) quantas letras tem o primeiro nome 
nome = str(input(" Digite seu nome completo: "))
print("Analisando seu nome...")
print("O seu nome é : {}".format(nome))
#a
print("O seu nome em maiusculo é: {}".format(nome.upper()))
#b
print("O seu nome minusculo é: {}".format(nome.lower()))
#c
print("Seu nome tem: {} letras".format(len(nome.replace(" ", ""))))
#d
print("O seu primeiro nome tem: {} letras".format(len(nome.split()[0])))