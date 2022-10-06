"""
Tipo String
"""
"""
Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '1234', 'a', 'True', '12.3';
- Estiver entre àspas duplas -> "uma string", "1234", "a", "True", "12.3";
- Estiver entre àspas simples triplas -> '''uma string''', '''1234''', '''a''', '''True''', '''12.3''';
"""
# - Estiver entre àspas duplas triplas -> """uma string""", """1234""", """a""", """True""", """12.3""";

name = 'João Pedro'  # O mais comum é utilizar àspas simples
print(name)
print(type(name))

name = 'Milena \nCosta'  # O \n serve para pular linha
print(name)

name = """Rosangela
Francisca"""  # Dessa forma também funciona para pular linha
print(name)

name = 'João \' Pedro'  # O caractere de escape " \ " antes da àspas serve para imprimir sem erro
print(name)
print(name.split())  # Trnasforma em  uma lista de strings

"""
O Python interpreta strings da seguinte maneira:
['J', 'o', 'ã', 'o', ' ', 'P', 'e', 'd', 'r', 'o']
[  0,   1,   2,   3,   4,   5,   6,   7,   8,  9 ]
"""
name = 'Testando array de strings'
print(name[0:5])  # Isso se chama Slice de strings
print(name[5:20])  # Isso se chama Slice de strings

name = 'João Pedro'
print(name.split()[0])  # Vai chamar somente 'João'
# ['João', 'Pedro']
# [   0  ,    1   ]
print(name.split()[1])  # Vai chamar somente 'Pedro'

"""
[::-1] -> Comece pelo primeiro elemento, vá até o último, e inverta no final: ordeP oãoJ.
"""
print(name[::-1])  # Inversão da string
print(name.replace('o', 'u'))

"""
Famoso Palíndromo de modo Pythônico
"""
text = 'socorram me subino onibus em marrocos'
print(text)
print(text[::-1])

text = 'ana'
print(text)
print(text[::-1])
