n=int(input("Digite um valor inteiro:\t"))
for x in range(0,11):
    print("n[{}] * x[{}] = {}".format(n,x,n*x))

for x in range(1,11):
    print("n[{}] / x[{}] = {}".format(n,x,n/x))

for x in range(0,11):
    print("n[{}] + x[{}] = {}".format(n,x,n+x))

for x in range(0,11):
    print("n[{}] - x[{}] = {}".format(n,x,n-x))

for x in range(0,11):
    print("n[{}] - x[{}] * x = {}".format(n,x,n-x*x))
print("Fim do programa.")