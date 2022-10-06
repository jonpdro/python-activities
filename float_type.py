"""
Tipo Float
"""
"""
Tipo real, decimal

Casas decimais

Obs: O separador de casas decimais na programação é o ponto e não vírgula.

# Errado do ponto de vista Float, mas gera uma tupla
value = 1,44

# Certo do ponto de vista Float
value = 1.44

# É permitido fazer a dupla atribuição
value1, value2 = 1, 44

value1 -> Recebe o valor de 1
value2 -> Recebe o valor de 44
"""
value = 1.50
print(type(value))
print(value)

# É possivel convert um float para um int
# TODO - Ao converter valores float para inteiros, nós perdemos precisão.
result = int(value)
print(result)

# É possivel trabalhar com números complexos, simbolizado pela letra J
number_complex = 5j
print(type(number_complex))
