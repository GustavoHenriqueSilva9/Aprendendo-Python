vet=[]
media=0
soma =0
maior=0
menor=0
acima=0
baixo=0
for i in range(0,5):
    vet.append(int(input("Informe a numero")))
    soma = soma + vet[i]
media = soma/5
acima= media*1.1
baixo=media-(media*0.1)

for i in range(0,5):
    if vet[i] >= (media*1.1):
      maior+=1
    if vet[i] <= (media - (media*0.1)):
      menor+=1
print("media e ",media)
print("10% acima da media: ",acima)
print("10% abaixo da media: ",baixo)
print("numeros de notas acima ",maior)
print("numeros de notas abaixo: ",menor)