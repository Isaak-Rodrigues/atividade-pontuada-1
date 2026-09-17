import os

os.system('cls')


renda = float(input('digite sua renda mensal: '))
parcelas = int(input('quantidade de parcelas:'))
emprestimo = int(input('deseja quanto de emprestimo:'))

if parcelas != renda *10 and emprestimo <= (renda * 0,3):
    print('não pode ser concedido')

else:
    print ('aprovado pelo banco')