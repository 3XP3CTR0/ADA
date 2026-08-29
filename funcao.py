from datetime import datetime

def dizer_hora():
    hora_atual = datetime.now()
    hora = hora_atual.strftime("%H:%M")
    return f"\nADA: Agora são {hora}.\n"

def dizer_data():
    data_atual = datetime.now()
    data = data_atual.strftime("%d/%m/%Y")
    return f"\nADA: Hoje é {data}.\n"