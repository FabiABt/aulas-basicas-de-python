# Faça um programa que leia uma frase pelo teclado e mostre A) quantas vezes apareçe a letra  "A".  
# B) Em que posição ela aparece a primeira vez  C) em qua posiçao ela aprece a ultima vez
frase = str(input(" Digite uma frase qualquer: "))
print("Na frase: {} a letra A apareçe {} vezes".format(frase, frase.count("a")))