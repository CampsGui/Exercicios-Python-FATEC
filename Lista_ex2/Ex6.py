total_bois = 0
total_peso_gordo = 0
total_peso_magro = 0
numero_boi_gordo = None
numero_boi_magro = None

n = int(input("Digite o número de bois na fazenda: "))
    
for i in range(n):
    numero = int(input("Digite o número do boi: "))
    peso = float(input("Digite o peso do boi: "))
    print("\n")
    
    total_bois += 1

    if numero_boi_gordo is None or peso > total_peso_gordo:
        total_peso_gordo = peso
        numero_boi_gordo = numero
    
    if numero_boi_magro is None or peso < total_peso_magro:
        total_peso_magro = peso
        numero_boi_magro = numero
    
print("Resultados da verificação:")
print("O boi mais gordo tem número", numero_boi_gordo, "e peso", total_peso_gordo, "Kg")
print("O boi mais magro tem número", numero_boi_magro, "e peso", total_peso_magro, "Kg")