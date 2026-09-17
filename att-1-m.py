import os

os.system('cls')

a = int(input('digite o primeiro numero'))
b = int(input('digite o segundo numero'))
c = int(input('digite o terceiro numero'))

soma = a + b

print('EXIBINDO DE DADOS')
print(f'soma  {soma} ')

if a and b > c:
    print('c e menor que A e B')

elif a and b < c:
    print('c e maior que A e B')
