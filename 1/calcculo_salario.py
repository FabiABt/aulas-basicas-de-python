
def calculo(valor, hora):
    sal_bruto = (valor_hora * hora_mes)
    ir = ((sal_bruto * 11) / 100)
    inss = ((sal_bruto * 8) / 100)
    sind = ((sal_bruto * 5 ) / 100)
    descontos = (sind + inss + ir)
    sal_liq = (sal_bruto - descontos)
    impressao(sal_bruto, ir, inss, sind, sal_liq)

def impressao(salario_bruto, ir, inss, sind, sal_liq):
    print("-Salário Bruto : R$ {:.2f}".format(salario_bruto))
    print("-IR (11%) : R$ {:.2f}".format(ir))
    print("-INSS (8%) : R$ {:.2F}".format(inss))
    print("-Sindicato (5%) : R$ {:.2f}".format(sind))
    print("-Salário Líquido : R$ {:.2f}".format(sal_liq))

quantidade_pessoas = int(input(" Para quantas pessoas voce dseja realizar o calculo do salário? "))
for i in range (0,quantidade_pessoas):
    valor_hora = float(input("Qual é o valor da hora trabalhada? "))
    hora_mes = int(input("Qual á a quantidade de horas trabalhadas no mês? "))
    calculo(valor_hora, hora_mes)