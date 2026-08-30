from datetime import datetime

def dizer_hora():
    hora_atual = datetime.now()
    hora = hora_atual.strftime("%H:%M")
    return f"\nADA: Agora são {hora}.\n"

def dizer_data():
    data_atual = datetime.now()
    data = data_atual.strftime("%d/%m/%Y")
    return f"\nADA: Hoje é {data}.\n"

def calcular(x, operador, y):

    while True:
        try:
            a = float(x)
            break  # Sai do laço se a conversão para float der certo
        except ValueError:
            return "Número inválido! Por favor, digite apenas números."

    while True:
        try:
            b = float(y)
            break  # Sai do laço se a conversão para float der certo
        except ValueError:
            return "Número inválido! Por favor, digite apenas números."

    if operador == "+":
        return f"O resultado da soma é {a + b}."

    elif operador == "-":
        return f"O resultado da subtração é {a - b}."

    elif operador == "*":
        return f"O resultado da multiplicação é {a * b}."

    elif operador == "/":
        if b == 0:
            return "Não é possível dividir por zero."
        return f"O resultado da divisão é {a / b}."

    else:
        return "Operador inválido."