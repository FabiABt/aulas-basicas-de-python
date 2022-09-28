# manipulando cadeias de texto
# FATIAMENTO
frase = "O michel faz programas em java, c#, kotlin, python e ele também joga dota"
print(frase)
#fatiamento 
  #dessa forma imprime apenas a letra na posição 9
print(frase[9])
  #fatiamento selecionando o inico e o fim da frase desejada ex [9:22] ela inicia com a letra na posiçao 9 e finaliza na posicão 21 
print(frase[9:22])
  #fatiamento selecionado o inicio e deixando ir ate o final da frase ex: [9:] , ele finaliza com a ultima letra da frase 
print(frase[9:])
  #fatiamento selecionando o inicio o fatiamento com o inico da frase ex: [:22] quando nao se coloca o inicio ele sempre considera o inicio na posição 0
print(frase[:22])
  # fatiamento com casas a ser "puladas"[9::3] ou seja vai pular 3 casas sendo ignorados os outros caracteres
print(frase[9::3])
  # ANALISE 
  # len(frase) analisa o compimento da frase 
print( len(frase))
  # .count() conta quantas letras selecionadas possue na frase , se quisermos saber quantas letras "a" por exemplo. ha diferença entre maiusculas e minusculas
print(frase.count("a"))
print(frase.count("a", 0,25))
  #frase.find("ama") vai dizer quantas vezes foi encontrada a sequencia "ama", vai indicar o momento em que começou a sequencia
print(frase.find("ama"))
# frase.find("ios") se colocar ums string que não existe ela vai retornar -1 
