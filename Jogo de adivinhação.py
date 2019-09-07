print("#####################################")
print("Bem vindo ao Jogo de Adivinhação!")
print("#####################################")
import random
numero_adivinhar = random.randrange(1,100)
print("Niveis de Dificuldade = (1)Facil, (2)Medio, (3)Dificil, (4)Muito Dificil")
dificuldade_jogo = int(input("Digite O Nivel de Dificuldade: "))
if (dificuldade_jogo == 1):
    total_tentativas = 10
    print("Nivel Facil Selecionado com Total de 10 Tentativas")
    print("------------------------------------------------------------")
elif (dificuldade_jogo == 2):
    total_tentativas = 6
    print("Nivel Medio Selecionado com Total de 6 Tentativas")
    print("------------------------------------------------------------")
elif (dificuldade_jogo == 3):
    total_tentativas = 4
    print("Nivel Dificil Selecionado com Total de 4 Tentativas")
    print("------------------------------------------------------------")
elif (dificuldade_jogo == 4):
    total_tentativas = 2
    print("Nivel Muito Dificil Selecionado com Total de 2 Tentativas")
    print("------------------------------------------------------------")
else:
    while ((dificuldade_jogo > 4) or (dificuldade_jogo < 1)):
        print("------------------------------------------------------------")
        print("Niveis de Dificuldade, (1)Facil, (2)Medio, (3)Dificil, (4)Muito Dificil")
        dificuldade_jogo = int(input("Digite um Nivel de Dificuldade Valido: "))
        if (dificuldade_jogo == 1):
            total_tentativas = 10
            print("Nivel Facil Selecionado com Total de 10 Tentativas")
            print("------------------------------------------------------------")
            break
        elif (dificuldade_jogo == 2):
            total_tentativas = 6
            print("Nivel Medio Selecionado com Total de 6 Tentativas")
            print("------------------------------------------------------------")
            break
        elif (dificuldade_jogo == 3):
            total_tentativas = 4
            print("Nivel Dificil Selecionado com Total de 4 Tentativas")
            print("------------------------------------------------------------")
            break
        elif (dificuldade_jogo == 4):
            total_tentativas = 2
            print("Nivel Muito Dificil Selecionado com Total de 2 Tentativas")
            print("------------------------------------------------------------")
            break
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

