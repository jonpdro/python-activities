"""
TODO - Enunciado
O aluno deverá criar um programa para informar se determinado número é primo ou não.
"""
# Entrada
number = int(input("Informe um número inteiro: "))
result = False

# Processamento
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            result = True
            break

# Saída
if result:
    print(f"O número informado pelo usuário NÃO é um número primo.")
else:
    print(f"O número informado pelo usuário é um número primo.")
