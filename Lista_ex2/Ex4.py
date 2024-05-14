while True:
    idade = int(input("Digite a idade: "))

    if idade <= 0:
        print("Idade inválida")
        break

    if idade < 18:
        print("Menor de Idade\n")
    elif idade < 65:
        print("Maior de Idade\n")
    else:
        print("Maior de 65 anos\n")