while True:
    valor_diaria = 0
    nome = input("Digite o nome do hóspede (ou 'sair' para encerrar): ")
    
    if nome.lower() == 'sair':
        print("Encerrando o programa...")
        break
    
    tipo_ap = input("Digite o tipo de apartamento que foi utilizado (A, B, C ou D): ").upper()
    diaria_num = int(input("Digite o número de diárias utilizadas pelo hóspede: "))
    valor_consumo = int(input("Digite o valor do consumo interno do hóspede: "))
    
    match tipo_ap:
        case 'A':
            valor_diaria = 250
        case 'B':
            valor_diaria = 150
        case 'C':
            valor_diaria = 100
        case 'D':
            valor_diaria = 75
    
    valort_diaria = diaria_num * valor_diaria
    subtotal = valort_diaria + valor_consumo
    taxa_servico = round((subtotal * (10/100)), 3)
    total_geral = round(subtotal + taxa_servico, 3)
    
    print("O valor total das diárias é igual a R$", valort_diaria)
    print("O subtotal é igual a R$", subtotal)
    print("O valor da taxa de serviço é igual a R$", taxa_servico)
    print("O total geral é igual a R$", total_geral)
    
    # Abrindo o arquivo para escrita e salvando os dados
    with open('dados_hospedes.txt', 'a') as arquivo:
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"Tipo de apartamento: {tipo_ap}\n")
        arquivo.write(f"Numero de diarias: {diaria_num}\n")
        arquivo.write(f"Valor do consumo interno: {valor_consumo}\n")
        arquivo.write(f"Valor total das diarias: {valort_diaria}\n")
        arquivo.write(f"Subtotal: {subtotal}\n")
        arquivo.write(f"Taxa de servico: {taxa_servico}\n")
        arquivo.write(f"Total geral: {total_geral}\n\n")