import random
tam = 100
vetor_numero =[int] * tam
#soma = 0
for i in range(len(vetor_numero)):
    vetor_numero[i] = random.randint(10,1000)  #i + 1

print(vetor_numero)