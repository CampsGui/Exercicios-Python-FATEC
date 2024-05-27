def encontrar_pivo(valores):
    valores_ordenados = sorted(valores)

    return valores_ordenados[1]
def main():
    exemplos = [
        "23 42 37 15",
        "15 30 15",
        "10 20 30"
    ]

    for entrada in exemplos:
        valores = list(map(int, entrada.split()))
        
        pivo = encontrar_pivo(valores)
        print(f"Entrada: {entrada} => Pivô: {pivo}")

if __name__ == "__main__":
    main()