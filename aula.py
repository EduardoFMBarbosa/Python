nota_1 = 0 # primeira nota do aluno
nota_2 = 0 # segunda nota do aluno
nome_aluno = ''

print(nota_1)
print(nota_2)
nota_1 = float(input('Informe a nota 1:'))
nota_2 = float(input('Informe a nota 2:'))
nome_aluno = input('Informe o nome do aluno:')
print(nota_1)
print(nota_2)
print(nome_aluno)
media = (nota_1 + nota_2)/2
print('A média do aluno:', nome_aluno, 'foi:', media)
if media>= 7:
    print('O aluno foi aprovado ', nome_aluno,' media:', media)
else:
    print('O aluno foi reprovado ', nome_aluno,' media:', media)

print('Fim do programa')