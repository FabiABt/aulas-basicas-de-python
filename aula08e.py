# faca um porograma que leia um angulo qualquer e mostre na tela o valor do sen0, cosseno e tangente desse angulo.
import math
angulo = float(input("Digito o valor do angulo que voce deseja: "))
seno = math.sin(math.radians(angulo))
print("O angulo de {} tem o Seno de {:.2f}".format(angulo, seno))
cos = math.cos(math.radians(angulo))
print("O angulo de {} tem o Cosseno de {:.2f}".format(angulo, cos))
tang =  math.tan(math.radians(angulo))
print("O angulo de {} tem a tangente de {:.2f}".format(angulo, tang))