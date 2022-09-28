# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos 
# ex digite um numero : 1834 ----- unidade: 4-- dezena 3. --- centena 8, ---- unidade de milhar 1.--
num = input("Digite um numero de zero a 9999: ")
if num == None:
    print("Fim do programa")
else:
    for i in range(len(num)-1,0,-1):
        if i == (len(num)-1):
            print("{} - unidade".format(num[i]))
        elif i == (len(num)-2):
            print("{} - dezena".format(num[i]))
        elif i == len(num)-3:
            print("{} - centena".format(num[i]))
        elif i == len(num)-4:
            print("{} - Und. milhar".format(num[i]))