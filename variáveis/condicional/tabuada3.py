tabuada=int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número ", tabuada)
comando = input("Digite um comando para a sua tabuada +, -, *, /: ")
print (" Tabuada do número {}".format(tabuada))
for valor in range(1,11):
    if comando == "+" :
        print(" {} {} {} = {} ".format(tabuada, comando, valor,tabuada+valor))
    elif comando == "-":
        print("  {} {} {} = {} ".format(tabuada, comando, valor,tabuada-valor))
    elif comando == "*":
        print("  {} {} {} = {} ".format(tabuada, comando, valor,tabuada*valor))
    else:
        print(" {} {} {}  =  {} ".format(tabuada, comando, valor,tabuada/valor))