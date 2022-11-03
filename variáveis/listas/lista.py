#Lista é uma coleção de valores indexada, em que cada valor é identificado por um índice. O primeiro item na lista 
# está no índice 0, o segundo no índice 1 e assim por diante.
secos = ['arroz', 'feijão', 'carne', 'linguiça', 'bife', 'suco']
horti_fruti = ['maça', 'banana', 'alface', 'tomate', 'brócolis']
laticinios = ['leite', 'queijo', 'iogurte', 'mussarela', 'requeijão']
secos.insert(2, 'açucar') # inserindo item na posição específica
secos[3] = 'café'  #Alteração em lista na posição específica
secos[4] = 'bolacha' #Alteração em lista na posição específica
for i in secos:
    print("+--------------------------------------------+")
    print("------------------ registro {} --------------------".format(i))
    print("Antes de inserir: {}".format(horti_fruti))
    horti_fruti.append(i)
    print("Depois de inserir de inserir: {}".format(horti_fruti))
    print("+--------------------------------------------+")
    
for i in laticinios:
    horti_fruti.append(i)