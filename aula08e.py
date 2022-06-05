# faca um porograma que leia um angulo qualquer e mostre na tela o valor do sen0, cosseno e tangente desse angulo.
from math import radians, sin, cos, tan
angulo = float(input("Digito o valor do angulo que voce deseja: "))
seno = sin(radians(angulo))
print("O angulo de {} tem o Seno de {:.2f}".format(angulo, seno))
cos = cos(radians(angulo))
print("O angulo de {} tem o Cosseno de {:.2f}".format(angulo, cos))
tang = tan(radians(angulo))
print("O angulo de {} tem a tangente de {:.2f}".format(angulo, tang))