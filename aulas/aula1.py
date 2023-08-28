# Atribuindo valor a uma variável
x = "Hello world"

# printar no console o valor
print(x)

# Mostrar o tipo da variável
print(type(x))

# Tipagem dinâmica
x = 2.7
print(type(x))

# Controle de fluxo
if x > 42:
    print("maior que a resposta da vida?")
elif x == 42:
    print("a resposta da vida!")
else: 
    print("Procurando a resposta da vida ainda...")

# Rode no terminal de python e rode `import this` para ver o guia da comunidade de como escrever python

# operações ambiguas não são possíveies (Ex.: somar inteiro com string, 
# transformo a string em inteiro e somo ou o inteiro em string e cocateno?)
a = 2
b = '3'
print(a + b)