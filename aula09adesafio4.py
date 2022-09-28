# crie um programa que leia o nome da pessoa e diga se ela tem ou Não  "Silva" no nome 
nome = input(" Digite seu nome: ")
name = ("silva" in nome.lower())
print(" no nome digitado {} e {} que possue Silva".format(nome, name))