SalarioAtual = float(input("Digite o salário atual: "))
pct = float(input("Digite o novo percentual de aumento: "))

aumento = SalarioAtual * (pct/100)
SalarioNovo = SalarioAtual + aumento

print("O aumento foi igual a R$ %.2f" % aumento)
print("O novo salário é igual a R$ %.2f" % SalarioNovo)