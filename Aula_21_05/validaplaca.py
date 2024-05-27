def format_string(input_string):
    # Converter todas as letras para maiúsculas
    input_string = input_string.upper()

    # Garantir que a string não exceda 50 caracteres
    if len(input_string) > 50:
        input_string = input_string[:50]

    # Verificar condição específica: sequência de três letras seguidas por 1 número, outra letra e por fim 2 números
    if len(input_string) == 7 and input_string[:3].isalpha() and input_string[3].isdigit() and input_string[4].isalpha() and input_string[-2:].isdigit():
        return "Placa Mercosul"

    # Verificar condição específica: sequência de três letras seguidas de quatro dígitos
    if len(input_string) == 7 and input_string[:3].isalpha() and input_string[3:].isdigit():
        return "Placa AAA-9999"

    # Verificar condição específica: sequência de duas letras seguidas de quatro dígitos
    if len(input_string) == 6 and input_string[:2].isalpha() and input_string[2:].isdigit():
        return "Placa AA-9999"

    # Verificar condição específica: sequência de até 7 números sem letras
    if input_string.isdigit() and len(input_string) <= 7:
        return "Placa numérica"

    # Verificar outra condição específica: uma letra ("A" ou "P") seguida por até 5 dígitos
    if len(input_string) > 1 and input_string[0] in ['A', 'P'] and input_string[1:].isdigit() and len(input_string[1:]) <= 5:
        return "Placa muito antiga"
    
    # Retornar "Placa inválida" se nenhuma condição for atendida
    return "Placa inválida"

# Exemplo de uso
input_string = input("Digite uma string com até 50 caracteres (apenas letras maiúsculas e dígitos): ")
resultado = format_string(input_string)
print(resultado)
