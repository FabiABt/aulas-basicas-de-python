nutricionistas = ['Fabiane', 'Livia', 'Mayara', 'Vanessa', 'Camilla', 'Camilla', 'Fernanda', 'Amanda', 'Julia']
print("o tipo é uma {}".format(type(nutricionistas))) # traz o tipo de variável
print("A lista possui {} nutricionistas".format(len(nutricionistas))) # traz o tamanho do objeto
sorteado = (int(input('Digite um numero de 0 a {}: '.format(len(nutricionistas)-1))))
print('A nutricionista sorteada foi : {}'.format(nutricionistas[sorteado]))
incluir = (str(input(" Digite um nome para adicionar a lista : ")))
nutricionistas.append(incluir)  # append() adiciona elementos no final de uma lista
print ( "A nova lista é : {}" .format(nutricionistas))
nutricionistas.insert(2,"Aline") ##### insert(). Ele usa dois parâmetros: 1* posição da lista 2* o item a ser adicionado na lista.
print(nutricionistas) 