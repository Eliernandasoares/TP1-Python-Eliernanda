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
        # Pedir ao usuário para inserir os números e a operação
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou seus nomes): ")

        # Chamar a função apropriada com base na operação
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

        # Imprimir o resultado
        print(f"Resultado da operação: {resultado}")

        # Perguntar se o usuário deseja continuar
        saida = input("Deseja continuar? (S/N): ")

        # Verificar se a entrada é válida
        if saida.lower() not in ['s', 'n']:
            print("Opção inválida! Digite S para continuar ou N para sair.")
            saida = input("Deseja continuar? (S/N): ")

# Chamar a função calculadora
calculadora()