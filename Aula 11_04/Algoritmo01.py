J01 = int(input("Escolha um número entre 1 a 10: "))
i=0
J02=i
if J01 <= 10:
    while not J01 == J02:
        J02 = int(input("Tente adivinhar o número que o jogador 1 escolheu(1 a 10): "))
    if J02 == J01:
        print("Parabéns, você adivinhou o número do jogador 1.")
else:
    print("Número Inválido")