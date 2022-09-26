#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
num = float(input("Digite um valor: "))
print("o valor digitado foi {} e sua porção inteira é {} ".format(num, trunc(num)))


# fazendo o mesmo exemplo sem importar bibliotecas 
num = float(input("Digite um valor qualquer"))
print("O o valor é {} e sua parte inteira é {}". format(num, int(num)))