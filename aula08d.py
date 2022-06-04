# crie um codigo que calcule a hipotenusa
co = int(input("Qual o valor do cateto oposto?"))
ca = int(input(" Qual o valor do cateto adjacent? "))
print("A hipotenusa vale : {}".format(pow (ca,2) + pow (co,2)))
# outra fornma de resolucao 
print("A hipotenusa vale : {}".format(co**2 + ca**2))
