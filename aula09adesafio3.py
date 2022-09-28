# crie um programa que leia o nome de uma cidade e diga se ela começa ou Não com o nome "Santo"
cidade = str(input( "Diginte o nome da sua cidade: "))
cid = ("santo" in cidade.lower())
print("O nome digitado é {} e é {} que possue a palavra Santo.".format(cidade, cid))