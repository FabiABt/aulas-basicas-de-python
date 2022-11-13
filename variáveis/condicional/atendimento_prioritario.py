# verificando se uma pessoa tem atendimento prioritario
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
gestante = (input( "Você está gestante? Digite S para sim e N para não: ")).upper()
deficiencia = (input("Você possui alguma dediciência de mobilidade? Digite S para sim e N para não: ")).upper()
if idade >= 65 or gestante == "S" or deficiencia == "S":
    print(" {} você possui atendimento prioritário! ".format(nome))
else:
    print(" {} você não possui atendimento prioritário! ".format(nome))