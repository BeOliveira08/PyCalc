def calculadora():
    print("Calculadora Simples")
    print("Operações: +, -, *, /")

    try:
        num1 = float(input("Digite o primeiro número: "))
        operador = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                resultado = "Erro: Divisão por zero"
            else:
                resultado = num1 / num2
        else:
            resultado = "Operador inválido"

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Erro: Por favor, digite números válidos")

# Executa a calculadora
calculadora()
