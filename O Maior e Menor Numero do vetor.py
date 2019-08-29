vetor = []
for i in range (0,3):
    vetor.append(int(input("Digite um numero Inteiro: ")))
numero_maior = 0
numero_menor = vetor[0]
for i in range (0,3):
    if numero_maior < vetor[i]:
        numero_maior = vetor[i]
    if numero_menor > vetor[i]:
        numero_menor = vetor[i]
print("Vetor: {} numero maior: {}, numero menor {} ".format(vetor,numero_maior,numero_menor))

