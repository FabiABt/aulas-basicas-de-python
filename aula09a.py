# manipulando cadeias de texto
# FATIAMENTO
frase = "O Michel faz programas em java, c#, kotlin, python e ele também joga dota"
print(frase)
#################### FATIAMENTO 
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
#################### ANALISE 
# len(frase) analisa o compimento da frase 
print( len(frase))
# .count() conta quantas letras selecionadas possue na frase , se quisermos saber quantas letras "a" por exemplo. ha diferença entre maiusculas e minusculas
print(frase.count("a"))
print(frase.count("a", 0,25))
#frase.find("ama") vai dizer quantas vezes foi encontrada a sequencia "ama", vai indicar o momento em que começou a sequencia
print(frase.find("ama"))
# frase.find("ios") se colocar ums string que não existe ela vai retornar -1 
print(frase.find("ios"))
# Usando o oparador   IN ex: "curso" in frase vai retornar um valor em bolleano (true or false)
print("curso" in frase)
print("joga" in frase)
##################### Transformação
# usando operador para mudar a saida da string, já que a string é imutável não substiue na frase original somente na saída/ frase.replace ("Michel", "Robson")
print(frase.replace("Michel","Robson"))
print(frase.replace("Michel", "vai Robson"))
# frase.upper() coloca as letas em caixa alta 
print(frase.upper())
# frase.lower() coloca tudo em caixa baixa 
print(frase.lower())
# frase.capitalize() coloca a primeira letra da frase em caixa alta e as demais letas em caixa baixa 
print(frase.capitalize())
# frase.title() coloca em caixa alta todas as primeiras letras de cada palavra
print(frase.title())
# exemplo com espaços vazios 
xs = "   O Michel faz piadas ruins  "
# frase.stripe.. nesse caso xs.strip elimina os espaços vazios das estremindades da frase
print(xs.strip())
# frase.rstrip() elimina espaçao vazios a direita ou seja no final da frase 
print(xs.rstrip())
#frase.lstrip elimina espaços vazios a esquerda 
print(xs.lstrip())
#########################FUNCIONALIDADE DE DIVISÃO 
# frase.split() ocorre uma divisão onde se tem os espaços, ou seja gera nova lista nas palavras e reconta casa elemento da nova lista 
print(xs.split())
#  "-".join(frase) todos os elementos de UMA LISTA utilizando o - entre elas (tem que ser LISTA ex: [casa, ,carro, bicilceta])
print('-'.join(frase))