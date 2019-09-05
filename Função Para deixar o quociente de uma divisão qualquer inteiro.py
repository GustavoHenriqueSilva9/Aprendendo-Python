def calc(numero,numero_dividido):
    divisao = numero / numero_dividido
    result = int(divisao)
    print("O Resultado da divisão é {}, e seu inteiro fica {}".format(divisao,result))
numero = int(input("Digite um numero para ser dividido: "))
numero_dividido = int(input("Dividido Por: "))
calc(numero,numero_dividido)