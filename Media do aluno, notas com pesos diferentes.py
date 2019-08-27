nome_aluno = input("Qual o nome do aluno?  ")
nota_1 = int(input("Digite a nota da primeira prova:  "))
nota_2 = int(input("Digite a nota da segunda prova:  "))
media_final = ((nota_1*2)+(nota_2))/3
print("A media do {} ficou {}".format(nome_aluno,round(media_final,2)))