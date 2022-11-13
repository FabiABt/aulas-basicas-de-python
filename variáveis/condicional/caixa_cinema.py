# escreva um programa para caixa de cinema. Seu programa deve recebera idade do usuario e se esta 'e estudante,
# com esses dados, exiba o preco d ingresso conforme a tabela 
# Estudante ou idoso (acima de 65 anos) pagam R$ 15,00
# Preco normal R$ 30,00
idade = int(input(" Qual é a sua idade? "))
estudante = input(" Você é estudante? responda com S para sim e N para não: ").upper()
entrada_normal= 30.00
if idade >= 65 or estudante == "S": 
    print( "O valor da entrada é {}".format(entrada_normal/2))
else :
    print("O valor da entrada é {}".format(entrada_normal))