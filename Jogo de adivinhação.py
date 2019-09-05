print("#####################################")
print("Bem vindo ao Jogo de Adivinhação!")
print("#####################################")
import random
numero_adivinhar = random.randrange(1,100)
total_tentativas = int(input("Digite o Numero de Tentativas para o Jogador Tentar Acertar: "))
print("=====================================================================")
for i in range (0,total_tentativas):
    chute = int(input("Chute um Número:  "))
    if(chute < 1 or chute > 100):
            print("Numero Invalido")
            print("Digite um numero entre 1 e 100")
            print("Restam {} Tentativas, de {} ".format(total_tentativas-i,total_tentativas))
            print("=====================================================================")
            continue
    else:
        if(chute > numero_adivinhar):
                print("VOCE ERROU, CHUTE UM NUMERO MENOR")
                print("Restam {} Tentativas de {} ".format(total_tentativas - i-1, total_tentativas))
                print("=====================================================================")
                continue
        elif(chute < numero_adivinhar):
                print("VOCE ERROU, CHUTE UM NUMERO MAIOR")
                print("Restam {} Tentativas de {} ".format(total_tentativas - i-1, total_tentativas))
                print("=====================================================================")
                continue
        elif(chute == numero_adivinhar):
                print("VOCE ACERTOU!!, PARABENS...")
                print("Restam {} Tentativas de {} ".format(total_tentativas - i-1, total_tentativas))
                print("=====================================================================")
                break
print("FIM DO PROGRAMA O NUMERO CERTO É {}".format(numero_adivinhar))

