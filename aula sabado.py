tam = 7
# 7(sete) elementos dentro do vetor = tam
# 6(seis) posições
vetor_numero =[int] * tam
#soma = 0
for i in range(len(vetor_numero)):
    vetor_numero[i] = int(input("Digite o valor \t"))
#[1,2,4,16,32,64,-128]
valor_a = vetor_numero[0]
valor_b = vetor_numero[0]
pos_menor = 0 #posição menor valor
pos_maior = 0 #posição maior valor
for i in range(len(vetor_numero)):
    #in = palavra neutra
    #range = de onde ele começa ate onde ele vai, faixa.
    #len = tamanho do vetor
    if vetor_numero[i] > valor_a:
        valor_a = vetor_numero[i]
        pos_maior = i
    if vetor_numero[i] < valor_b:
        valor_b = vetor_numero[i]
        pos_menor = i

    #soma = soma + vetor_numero[i]

print("O resultado de valor_a ", valor_a)
print("A posição do maior valor ", pos_maior)
print("O resultado de valor_b ", valor_b)
print("A posição do menor valor ", pos_menor)