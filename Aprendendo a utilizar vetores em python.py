vet = []
soma = 0
pares = 0
quantidade_pares = 0
acima_media = 0
for i in range (0,5):
    vet.append(int(input("informe a Notas: ")))
    soma = soma + vet[i]
    if (vet[i] % 2 == 0):
        pares = pares + vet[i]
        quantidade_pares = quantidade_pares + 1
if (quantidade_pares == 0):
        print("Nao existe Numeros Pares")
else:
        print("media dos numeros pares {}".format(pares / quantidade_pares))
print("soma dos elementos é {}".format(soma))
soma_media = soma / 5
for i in range (0,5):
    if (vet[i] > soma_media):
        acima_media = acima_media + 1
print("quantidade a cima da media {}".format(acima_media))