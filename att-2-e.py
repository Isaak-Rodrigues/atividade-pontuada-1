import os

os.system('cls')

nome = (input('digite seu nome. '))
genero = (input('digite seu genero. '))
estado_civil = (input('digite seu estado civil. '))

if genero == 'feminino' and estado_civil == 'casada':
    tempo_de_casada = input('digite tempo de casado')


print(f'\n nome  {nome} ')
print(f' genero  {genero} ')
print(f' estado_civil  {estado_civil } ')
print(f'tempo_de_casada {tempo_de_casada } ')