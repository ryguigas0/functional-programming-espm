lista = [
    {'nome': 'João', 'idade': 31},
    {'nome': 'Maria', 'idade': 37},
    {'nome': 'José', 'idade': 26}
]

def processar(lista, processamento):
    for i in lista:
        print(processamento(i))

processar(lista, lambda p: f"{p['nome']} tem {p['idade']} anos")