import os

os.system('cls')

primeiro_numero = float(input('digite o primeiro numero. '))
segundo_numero = float(input('digite o segundo numero. '))
operacao = str(input('escolha a operação. '))

soma = primeiro_numero + segundo_numero
subtracao =  primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero


match operacao:
    case '+':
        print(f'a soma dos numeros {primeiro_numero} + {segundo_numero} = {soma}')
    case '-':
        print(f'a subtração dos numeros {primeiro_numero} - {segundo_numero} = {subtracao}')
    case '*':
        print(f'a multiplicação dos numeros {primeiro_numero} * {segundo_numero} = {multiplicacao}')
    case '/':
        print(f'a divisão dos numeros {primeiro_numero} / {segundo_numero} = {divisao}')
