def calc_media(vet):
    m=0
    for i in range (0,5):
        m += vet[i]
    m = m/5
    return m
def calc_maior(valor):
    maior_valor = vet[0]

    for i in range(0,5):
        if (vet[i] > maior_valor):
            maior_valor = vet[i]
    return maior_valor
vet = []
for i in range (0,5):
    vet.append(int(input("Digite um valor para seu vetor:  ")))
media = calc_media(vet)
maior = calc_maior(vet)
print("A MEDIA DOS NUMEROS DIGITADOS NO VETOR É: {}, COM O MAIOR VALOR DE {}".format(media,maior))

