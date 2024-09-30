def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

def calculadora():
    saida = ''
    while saida.lower() != 'n':
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou seus nomes): ")
        if operacao in ['+', 'soma']:
            resultado = adicao(a, b)
        elif operacao in ['-', 'subtração']:
            resultado = subracao(a, b)
        elif operacao in ['*', 'multiplicação']:
            resultado = multiplicacao(a, b)
        elif operacao in ['/', 'divisão']:
            resultado = divisao(a, b)
        else:
            resultado = "Erro: operação inválida"
        print(f"Resultado da operação: {resultado}")
        saida = input("Deseja continuar? (S/N): ")
        if saida.lower() not in ['s', 'n']:
            print("Opção inválida! Digite S para continuar ou N para sair.")
            saida = input("Deseja continuar? (S/N): ")
calculadora()
