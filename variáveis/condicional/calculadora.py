#Faça um programa que leia um código de operação (+,-,* ou /), e também dois valores inteiros A e B. O programa deve calcular o resultado
#  da operação escolhida aplicado a A e B. Por exemplo, se a operação escolhida foi * e A = 1 e B = 3, 
# o programa deve fornecer como resultado o valor de 1*3, que é 3.
n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite outro valor inteiro: "))
comando = input("Digite um comando +,-,* ou /:  ")
if comando == "+" :
    print(" o valor {} {} {} é igual a {} ".format(n1, comando, n2,n1+n2))
elif comando == "-":
    print(" o valor {} {} {} é igual a {} ".format(n1, comando, n2,n1-n2))
elif comando == "*":
    print(" o valor {} {} {} é igual a {} ".format(n1, comando, n2,n1*n2))
else:
    print(" o valor {} {} {} é igual a {} ".format(n1, comando, n2,n1/n2))