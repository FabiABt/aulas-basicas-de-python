n1 = float(input("digite um valor"))
n2 = float(input("digite outro valor"))
c = input("digite um comando")

if c=="+":
    print(n1+n2)
elif c=="-":
    print(n1-n2)
elif c=="*":
    print(n1*n2)
elif c=="/":
    print( n1/n2)
else:
    print("Operacao nao permitida")