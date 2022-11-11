#Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre o peso ideal, 
# utilizando as seguintes fórmulas (onde h corresponde à altura): homens(72,7*h)-58//  mulheres:(62,1*h)-44,7
estatura = float(input("Qual é a sua estaura em metro? "))
sexo = (input(" Qual é o seu sexo ? responda com M para masculino e F para feminino: "))
sexo = sexo.upper()
if sexo == "M":
    print("Seu peso ideal é:  {}".format((72.7*estatura)-58))
else:
    print("Seu peso ideal é: {}".format((62.1*estatura)-44.7))