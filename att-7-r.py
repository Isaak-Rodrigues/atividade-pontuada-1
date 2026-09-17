import os

os.system('cls')

nome = str(input('digite o nome. '))
quantidade = str(input('digite a quantidade. '))
preço_unitario = str(input('digite o preço_unitario. '))

valor_final = quantidade * preço_unitario

if quantidade <= 5:
    print(f'valor a pagar: {valor_final / 0.02}')

elif quantidade > 5 and quantidade <= 10:
    print(f'valor a pagar: {valor_final / 0.03}')

elif  quantidade > 10:
    print(f'valor a pagar: {valor_final / 0.03}')