while True:
    numero = int(input("Digite um número inteiro (ou digite 0 para sair): "))
    if numero == 0:
        break

    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

    if not primo:
        divisores = []
        divisor = 2
        while divisor <= numero // 2:
            if numero % divisor == 0:
                divisores.append(divisor)
            divisor += 1

        if len(divisores) == 1 and divisores[0]**2 == numero:
            print("\nsim")
            print(f"\n{numero} é um 'primo de mentirinha'! É divisível por 1, {divisores[0]}, e {numero}.\n")
        else:
            print("\nnão\n")
    else:
        print("\nnão\n")
