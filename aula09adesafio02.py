# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos 
# ex digite um numero : 1834 ----- unidade: 4-- dezena 3. --- centena 8, ---- unidade de milhar 1.--
nume = int(input("Digite um numero de zero a 9999: "))
u = nume // 1 % 10
d = nume // 10 % 10
c = nume // 100 % 10
m = nume // 1000 % 10 
print(" Analisando o numero {}".format(nume))
print(" Unidade: {}".format(u))
print(" Dezena: {}".format(d))
print(" Centena: {}".format(c))
print(" Unidade de milhar: {}".format(m))