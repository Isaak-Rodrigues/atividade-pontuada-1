import os

os.system('cls')

print('Combustível |  	Quantidade Vendida	 |Desconto por Litro')
print('Álcool      |    Até 25 litros	         |     10%')
print('Álcool	     |   Acima de 25 litros	     |     20%')
print('Gasolina	 |     Até 25 litros	     |     15%')
print('Gasolina	 |   Acima de 25 litros      |     30%')

combustivel = str(input('digite (A) para alcool e (G) para gasolina. '))
litros = int(input('digite quantos litros deseja. '))
valor_alcool = 3.78
valor_gasolina = 6.59

match combustivel:
  case 'A':
    valorA = valor_alcool * litros
    if litros <= 25:
      print (f'valor a pagar no alcool: {valorA / 0.10}')
    else:
      print (f'valor a pagar no alcool: {valorA / 0.20}')
  case 'G':
    valorG = valor_gasolina * litros
    if litros <= 25:
      print (f'valor a pagar no gasolina: {valorG / 0.15}')
    else:
      print (f'valor a pagar no gasolina: {valorG / 0.30}')
      


