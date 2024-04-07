kmPercorrido = int(input("\nInforme quantos quilometros foram percorridos: "))
combustivel = int(input("\nInforme quanto combustivel foi consumido: "))

taxaConsumo = kmPercorrido / combustivel

print("\nO automóvel consome %.1f Km/l" % taxaConsumo)

if taxaConsumo <= 8:
    print("\nO automovel está consumindo muito combustivel")
else:
    print("\nO consumo de combustivel está bom")