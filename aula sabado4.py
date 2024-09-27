tam = 50
vetor_numero = [int] * tam
soma = 0
for i in range(len(vetor_numero)):
    vetor_numero[i] = i + 1
    soma = soma + vetor_numero[i]

print(vetor_numero)
print('A soma dos valores do vetor é:', soma)