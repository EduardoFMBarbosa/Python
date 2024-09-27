tam = 8
vetor_vetor1 =[int] * tam
soma = 0 
valor_pos_1 = 0  #X
valor_pos_2 = 0  #Y
for i in range(len(vetor_vetor1)):
    vetor_vetor1[i] = int(input("Digite o valor \t"))
valor_pos_1 = int(input("Digite a primeira posição \t")) #X
valor_pos_2 = int(input("Digite a segunda posição \t")) #Y
for i in range(len(vetor_vetor1)):
    if valor_pos_1 == i:
        soma = soma + vetor_vetor1[i]
    if valor_pos_2 == i:
        soma = soma + vetor_vetor1[i]
print(vetor_vetor1)
print(vetor_vetor1[valor_pos_1])
print(vetor_vetor1[valor_pos_2])
print("A soma do conteudo posições", valor_pos_1, valor_pos_2, "é:" , soma)