def normal_romano(num):
    # Converte números normais para números romanos
    valor = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    simbolo = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    num_romano = ''
    i = 0
    while num > 0:
        for _ in range(num // valor[i]):
            num_romano += simbolo[i]
            num -= valor[i]
        i += 1
    return num_romano


def romano_normal(romano):
    # Converte números romanos para números normais
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num_normal = 0
    val_anterior = 0
    for char in reversed(romano):
        value = roman_dict[char]
        if value < val_anterior:
            num_normal -= value
        else:
            num_normal += value
        val_anterior = value
    return num_normal


def main():
    while True:
        print("\nEscolha a operação:")
        print("1 - Converter número normal para romano")
        print("2 - Converter número romano para normal")
        print("0 - Sair")
        escolha = input("Digite o número da operação desejada: ")

        if escolha == '1':
            num = int(input("Digite o número normal: "))
            result = normal_romano(num)
            print(f"O número romano correspondente é: {result}")
        elif escolha == '2':
            roman = input("Digite o número romano: ")
            result = romano_normal(roman.upper())
            print(f"O número normal correspondente é: {result}")
        elif escolha == '0':
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
