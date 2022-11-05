idade= int(input("digite sua idade: "))
if idade <= 12:
    print("Você é criança")
elif idade < 20: 
    print("Você é jovem")
elif 20 <= idade < 60:
    print("Você é Adulto ")
else: 
    print("Você é idoso")