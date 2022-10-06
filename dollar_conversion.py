"""
TODO - Enunciado
O aluno deverá criar um programa para realizar a conversão de reais em dólares.
"""
# Entrada
amount_of_reais = float(input("Informe a quantidade de reais para conversão: "))
dollar_quote = float(input("Informe a cotação do dolár atual: "))

# Processamento
result = amount_of_reais / dollar_quote

# Saída
print(f"\nO valor em reais convertidos em doláres é de: {result}")
