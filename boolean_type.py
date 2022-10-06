"""
Tipo Booleano
"""
"""
Algebra Booleana, criada por George Boole

Todo -> 2 constantes, verdadeiro (True) ou valso (False)

Obs: Sempre com a inicial maiúscula

# Errado
true, false

# Correto
True, False
"""
active = True
print(f"Verdadeiro ou Falso: {active}")

"""
Operações básicas:

# Negação (not):
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso. Se for falso, o resultado será verdadeiro.
Ou seja, sempre o contrário
"""
print(f"Operação Negação (not): {not active}")

"""
# Ou (or):
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
logged = True
print(f"Operação Ou (or): {active or logged}")

"""
# E (and):
Também é uma operação binária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiro.

True or True -> True
True or False -> False
False or True -> False
False or False -> False
"""
print(f"Operação E (and): {active and logged}")
