total_s = 0
total_n = 0
total_f = 0
total_m = 0
total_entrevistados = 0
    
n = int(input("Digite o número de entrevistados: "))
    
for i in range(n):
        sexo = input("Digite o sexo do entrevistado (M/F): ").upper()
        resposta = input("Você gostou do produto? (S/N): ").upper()
        
        if resposta == "S":
            total_s += 1
            if sexo == "F":
                total_f += 1
        elif resposta == "N":
            total_n += 1
            if sexo == "M":
                total_m += 1
        
        total_entrevistados += 1
    
        percentual_s_f = (total_f / total_entrevistados) * 100
        percentual_n_m = (total_m / total_entrevistados) * 100
    
print("\nResultados da pesquisa:")
print("Total de entrevistados que responderam sim:", total_s)
print("Total de entrevistados que responderam não:", total_n)
print("Porcentagem de entrevistadas do sexo feminino que responderam sim: {:.2f}%".format(percentual_s_f))
print("Porcentagem de entrevistados do sexo masculino que responderam não: {:.2f}%".format(percentual_n_m))