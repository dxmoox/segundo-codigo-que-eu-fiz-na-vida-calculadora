valor1 = 0
valor2 = 0
resultado = 0
operacao = ''

valor1 = int(input('digite o valor1: '))
operacao = input('digite a operacao: ')
valor2 = int(input('digite o valor2: '))

if operacao == '+':
        resultado = valor1 + valor2
elif operacao == '-':
        resultado = valor1 - valor2
elif operacao == '*':
        resultado = valor1 * valor2
elif operacao == '/':
        resultado = valor1 / valor2

print(valor1,operacao,valor2,'=',resultado)
