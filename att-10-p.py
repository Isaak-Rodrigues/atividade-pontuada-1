import os

os.system('cls')

print('Combustível |  	Quantidade Vendida	   |Desconto por Litro')
print('Álcool      |    Até 25 litros	         |     10%')
print('Álcool	     |   Acima de 25 litros	     |     20%')
print('Gasolina	   |     Até 25 litros	       |     15%')
print('Gasolina    |   Acima de 25 litros      |     30%')

combustivel = str(input('digite (A) para alcool e (G) para gasolina. '))
litros = int(input('digite quantos litros deseja. '))
valor_alcool = 3.78
valor_gasolina = 6.59

match combustivel:
    case 'a' | 'A':
        valorA = valor_alcool * litros
        if litros <= 25:
         total = valorA * 0.90
        else:
            total = valorA * 0.80
        print(f'Valor a pagar no álcool: R$ {total}')
    
    case 'g' | 'G':
        valorG = valor_gasolina * litros
        if litros <= 25:
            total = valorG * 0.85
        else:
            total = valorG * 0.70
        print(f'Valor a pagar na gasolina: R$ {total}')
    
    case _:
        print('Opção inválida! Digite a ou g.')



