# crie um programa que leia o nome completo de uma pessoa e mostre:
# a) o nome com trodas as letras maiusculas
# b) o nome com todas as letras em caixa baixa 
# c) quantas letras tem o nome sem considerar os pepaços
# d) quantas letras tem o primeiro nome 
nome = str(input(" Digite seu nome completo: ")).strip()
print("Analisando seu nome...")
print("O seu nome é : {}".format(nome))
#a
print("O seu nome em maiusculo é: {}".format(nome.upper()))
#b
print("O seu nome minusculo é: {}".format(nome.lower()))
#c
print("Seu nome tem: {} letras".format(len(nome.replace(" ", ""))))
# forma resolvida pelo professor foi a descrita abaixo: 
print("Seu nome tem: {} letas".format(len(nome)- nome.count(" ")))
#d
print("O seu primeiro nome tem: {} letras".format(len(nome.split()[0])))
#forma resolvida pelo professor :
print("Seu primeiro nome tem {} letras".format(nome.find(" ")))