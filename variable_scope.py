"""
Escopo de variáveis
"""
"""
Dois casos de escopo:

1 - Variáveis globais;
        -> Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.
2 - Variáveis locais;
        -> Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado
        ao bloco onde foi declarada.
        
Declarando variavel no Python:
nome_variavel = valor_variavel

Python é uma linguagem de tipagem dinâmica. Ou seja, ao declarar uma variável, nós não colocamos o tipo de dado nela.
Este tipo é inserido ao atribuímos o valor à mesma.

Exemplo em Java:
String name = "João Pedro";
int number = 27;

No Python é possível fazer uma reatribuição de valor à uma váriavel independente do seu tipo.
"""
number = 27  # Exemplo de variável global
print(number)
print(type(number))

number = False  # Exemplo de reatribuição
print(number)
print(type(number))

number = 27

if number > 10:
    new = number + 10  # A variável new é definida dentro do escopo if, sendo assim, uma variável local
    print(new)

print(new)
"""
O Python reconhece a váriavel 'new' e exibe ela na tela, mas ele permance insistindo avisando que a variável não está 
declarada em um escopo global. "Name 'new' can be undefined".
"""
