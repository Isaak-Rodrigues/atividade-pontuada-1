import os

os.system('cls')

import os

cor = input("Digite a cor do CD (Verde, Azul, Amarelo, Vermelho): ").strip().lower()

match cor:
    case "verde":
        print("O preço do CD é: R$ 10,00")
    case "azul":
        print("O preço do CD é: R$ 20,00")
    case "amarelo":
        print("O preço do CD é: R$ 30,00")
    case "vermelho":
        print("O preço do CD é: R$ 40,00")
    case _:
        print("Cor inválida! Escolha entre Verde, Azul, Amarelo ou Vermelho.")