import os

os.system('cls')

primeiro_nota = float(input('digite a primeira nota.  '))
segundo_nota = float(input('digite a segunda nota. '))


media = ('primeiro_nota + segundo_nota')


if media <= 4.0:
    print('aluno reprovado')

elif  media <= 5.9:
    print('aluno em recuperação')

elif media >= 5.9:
    print('aluno aprovado')