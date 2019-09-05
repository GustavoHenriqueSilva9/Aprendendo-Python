vetor = []
quantidade = 0
media_final = 0
resultado = 0
def media_impares(vetor):
    soma = 0
    quantidade = 0
    for i in range (0,5):
        if vetor[i] % 2 != 0:
            soma += vetor[i]
            quantidade += 1
        media_final = soma / quantidade
    return media_final
for i in range(0,5):
    vetor.append(int(input("Digite um numero inserir no Vetor: ")))
resultado = media_impares(vetor)
print("##############################")
print("A Media dos Numeros pares é {}".format(resultado))
print("##############################")


