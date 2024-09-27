tam = 6
vetor_X = [int] * tam
vetor_Y = [int] * tam
for i in range(len(vetor_X)):
    vetor_X[i] = int(input("Digite o valor \t"))
for j in range(len(vetor_Y)):
    vetor_Y[j] = vetor_X[i]
    i = i -1
print("O vetor X", vetor_X)
print("O valor Y", vetor_Y) 