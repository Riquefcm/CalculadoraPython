def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b

while True:
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    operacao = input("Escolha a operação (+, -, *, /): ")

    if operacao == '+':
        print(f"Resultado: {adicao(num1, num2)}")
    elif operacao == '-':
        print(f"Resultado: {subtracao(num1, num2)}")
    elif operacao == '*':
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif operacao == '/':
        print(f"Resultado: {divisao(num1, num2)}")
    else:
        print("Operação inválida, por favor escolha +, -, *, ou /.")
        continue

    outra_operacao = input("Deseja realizar outra operação? (s/n): ").lower()
    if outra_operacao != 's':
        break
