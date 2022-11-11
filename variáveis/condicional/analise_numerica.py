#Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. 
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
from math import sqrt
numero =float(input("Digite um número qualquer: "))
if numero >= 0:
    print (" A raiz quadrada de {} é {} .".format(numero, sqrt(numero)))
else:
    print(" O número é inválido.")