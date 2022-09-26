# crie um codigo que calcule a hipotenusa
import math
co = float(input("Qual o valor do cateto oposto? "))
ca = float(input(" Qual o valor do cateto adjacente? "))
hi = math.hypot(co,ca)
print("A hipotenusa vale : {}".format(hi))
# outra fornma de resolucao 
print("A hipotenusa vale : {}".format((co**2 + ca**2)**(1/2)))