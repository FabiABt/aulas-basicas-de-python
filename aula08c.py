from math import trunc
num = float(input("Digite um termo real: "))
print(" o numero {} tem a parte inteira {}.".format(num,int(num)))
print (" o numero {} tem a parte inteira {}.".format(num, trunc(num)))
# tem as duas formar de resolucao sendo chamando o trunc e atrubuindo  inteiro na parte num digitado 