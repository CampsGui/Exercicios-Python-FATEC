print("CÓDIGO	ESPECIFICAÇÃO	PREÇO UNITÁRIO(R$)"
"\n1	Cachorro quente	8,10"
"\n2	Bauru simples	11.30"
"\n3	Bauru c/ovo     15,50"
"\n4	Hamburger       13.10"
"\n5	Cheeseburger	14.30"
"\n6	Refrigerante	5.00"
)

codigo=int(input("Informe o código do item pedido: "))
match codigo:
    case 1:
        print("\nCachorro quente")
        qtd=int(input("Digite a quantidade comprada: "))
        valor = qtd * 8.10
        print("\nValor a ser pago: R$ %.2f" % valor)
    case 2:
        print("\nBauru simples")
        qtd=int(input("Digite a quantidade comprada: "))
        valor = qtd * 11.30
        print("\nValor a ser pago: R$ %.2f" % valor)
    case 3:
        print("\nBauru c/ovo")
        qtd=int(input("Digite a quantidade comprada: "))
        valor = qtd * 15,50
        print("\nValor a ser pago: R$ %.2f" % valor)
    case 4:
        print("\nHamburger")
        qtd=int(input("Digite a quantidade comprada: "))
        valor = qtd * 13.10
        print("\nValor a ser pago: R$ %.2f" % valor)
    case 5:
        print("\nCheeseburger")
        qtd=int(input("Digite a quantidade comprada: "))
        valor = qtd * 14.30
        print("\nValor a ser pago: R$ %.2f" % valor)
    case 6:
        print("\nRefrigerante")
        qtd=int(input("Digite a quantidade comprada: "))
        valor = qtd * 5.00
        print("\nValor a ser pago: R$ %.2f" % valor)
    case _:
        print("\nCódigo Invalido")