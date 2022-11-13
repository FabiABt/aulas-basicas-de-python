nome=input("Digite o seu nome: ")
idade=int(input("Digite a sua idade: "))
gestante = (input( "Você está gestante? Digite S para sim e N para não: ")).upper()
deficiencia = (input("Você possui alguma dediciência de mobilidade? Digite S para sim e N para não: ")).upper()
febre = (input("Sua temperatura é maior que 37*C? digite S para sim e N para não: ")).upper()
Dor_cabeça  = (input("Você esta sentindo dor de cabeça ício súbito ou rapidamente progressiva? digite S para sim e N para não: ")).upper()
asma = (input("Você esta em crise asmática? digite S para sim e N para não: ")).upper()
emese = (input("Você esta sentindo nauseas/ vômito? digite S para sim e N para não: ")).upper()
dor_abominal = (input("Você esta sentindo dor abdominal? digite S para sim e N para não: ")).upper()
evacuacao = (input("Você evacuou nas ultimas 24 horas? digite S para sim e N para não: ")).upper()
sangue = (input("Você houve presença de sangue nas fezes? Digite S para sim e N para não: ")).upper()
queda =(input("Você bateu a cabeça ? digite S para sim e N para não: ")).upper()
desmaio = (input("Você esta desmaiou/ perdeu a consiência? digite S para sim e N para não: ")).upper()

if idade>=65:
    prioridade="SIM"
print("O paciente " + nome + " possui atendimento prioritário? " + prioridade)