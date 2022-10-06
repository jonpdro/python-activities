"""
Recebendo dados do usuário
"""
"""
input() -> Todo dado recebido via input é do tipo String

Em Python, tudo que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simples -> 'Milena Costa'
- Aspas duplas -> "Milena Costa"
- Aspas simples triplas -> '''Milena Costa'''
"""
# - Aspas duplas triplas -> """Milena Costa"""

# Entrada de dados
# print("Qual é o seu nome?")
# name = input()  # Input -> Entrada
name = input("Qual é o seu nome? ")

# Exemplo de print 'antigo' (v2.x)
# print("\nSeja bem-vindo(a) %s!\n" % name.title())

# Exemplo de print 'recente' (v3.x)
# print("\nSeja bem-vindo(a) {0}!\n".format(name.title()))

# Exemplo de print 'mais recente' (v3.7^)
print(f"\nSeja bem-vindo(a) {name.title()}!")

# print("\nQual é a sua idade?")
# age = input()
age = int(input("\nQual é a sua idade? "))

# Processamento

# Saída de dados
# Exemplo de print 'antigo' (v2.x)
# print("\nA %s tem %s anos!" % (name.title(), age))

# Exemplo de print 'recente' (v3.x)
# print("\n{0} tem exatos {1} anos de idade!".format(name.title(), age))

# Exemplo de print 'mais recente' (v3.7^)
print(f"\n{name.title()} tem exatos {age} anos de idade!")
"""
int() -> cast

cast é a "conversão" de um tipo de dado para outro.
"""
print(f"{name.title()} nasceu em {2022 - age}.")
