tam = 10
vetor_vetor1 =[int] * tam
vetor_vetor2 =[int] * tam
for i in range(len(vetor_vetor1)):
    vetor_vetor1[i] = int(input("Digite o valor \t"))
    #print(vetor 1)
    #[1,6,8,12,..]
    #[1,4,9,16,..]
    print(vetor_vetor1)
print(vetor_vetor1)
for j in range(len(vetor_vetor2)):
    vetor_vetor2[j] = (vetor_vetor1[j] * vetor_vetor1[j])

print(vetor_vetor1)
print(vetor_vetor2)     