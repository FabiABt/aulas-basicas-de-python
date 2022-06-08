#Variáveis em Python são lugares reservados na memória de um dispositivo para o armazenamento de dados que posteriormente vão ser usados na execução de uma solução digital.
#Para declarar as variáveis no Python, é preciso seguir algumas regrinhas: unca deve nomear uma variável começando com um número ou símbolo (5 ou %, por exemplo), mas sim com uma letra minúscula ou underline.
#é não utilizar palavras reservadas 
# tipos de variaveis : str, int, float, complex, bool, list, tuple, dict
num = 5 # int
n1 = 3.5 #float
print(num)
print(type(num))
print(n1)
print(type(n1))
soma =  num + n1
print(soma)
print(type(soma))
aluna = 'Maria' #str
print(aluna)
print(type(aluna))
nome = ['maria', 'joao', 'pedro', 'marcos']
print(nome)
print(type(nome))
#como mudar o tipo de uma variavel 
altura =1.80
print(altura)
print(type(altura))
altura = str(altura)
print(type(altura))