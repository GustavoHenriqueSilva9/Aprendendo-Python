vetor = []
for i in range (0,5):
    vetor.append(int(input("Digite um numero para o vetor: ")))
vetor_r = vetor[::-1]
print("VETOR NORMAL: {}, VETOR INVERSO: {}".format(vetor,vetor_r))