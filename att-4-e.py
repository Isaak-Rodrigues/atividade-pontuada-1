import os

os.system('cls')

print('selecione uma fruta: ')
print('1- maçã')
print('2- morango')

opcoes = input('digite o numero da fruta')

kg_morango = float(input("Digite a quantidade de morangos (em Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (em Kg): "))


if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

# Cálculo do preço das maçãs
if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

peso_total = kg_morango + kg_maca
valor_total = preco_morango + preco_maca

if peso_total >= 10 or valor_total > 15.00:
    valor_total = valor_total * 0.90

print(f"Valor a ser pago pelo cliente: R$ {valor_total:.2f}")


