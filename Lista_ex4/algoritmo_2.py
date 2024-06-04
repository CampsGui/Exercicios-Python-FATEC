aprovadas = 0
reprovadas = 0
p_reprovadas = []

while True:
    num_p = input("Digite o número da peça (ou 'sair' para encerrar): ")
    if num_p.lower() == 'sair':
        break
    
    estado = input("Digite o estado da peça (aprovado ou reprovado): ").lower()
    
    if estado == "reprovado":
        p_reprovadas.append(num_p)
        reprovadas += 1
    else:
        aprovadas += 1
    
    if aprovadas + reprovadas >= 800:
        print("Capacidade máxima de produção atingida.")
        break

print("Números das peças reprovadas:")
for p in p_reprovadas:
    print(p)

print("Total de peças aprovadas:", aprovadas)
print("Total de peças reprovadas:", reprovadas)