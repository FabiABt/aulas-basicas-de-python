#As maçãs custam R$0,30 cada se forem compradas menos do que uma dúzia, e R$0,25 se forem compradas pelo menos doze. 
# Escreva um programa que leia o número de maçãs compradas, calcule e escreva o valor total da compra.
macas = int(input(" Qantas maçãs você deseja comprar? "))
if macas <= 11:
    print(" O valor da sua compra é: {:.2f} R$".format(macas * 0.30))
else:
    print("O valor da sua compra é: {:.2f} R$".format(macas *0.25))