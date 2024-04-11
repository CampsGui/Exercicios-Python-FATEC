contador=0

J01 = int(input("Escolha um número entre 1 a 10: "))

while J01 < 1 or J01 > 10:
    print("\nPor favor, escolha um número entre 1 e 10.")
    J01 = int(input("\nEscolha um número entre 1 a 10: "))

J02=0

while J01 != J02:
    J02 = int(input("\nJogador 2, tente adivinhar o número que o jogador 1 escolheu (1 a 10): "))
    contador += 1
    
    while J02 < 1 or J02 > 10:
        print("\nPor favor, escolha um número entre 1 e 10.")
        J02 = int(input("\nJogador 2, tente adivinhar o número que o jogador 1 escolheu (1 a 10): "))
    
print("\nParabéns, você adivinhou o número do jogador 1")
print("Número de tentativas:", contador)
