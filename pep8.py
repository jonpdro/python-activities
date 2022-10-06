"""
PEP8 - Python Enhancement Proposal
"""
import this
"""
São propostas de melhorias para a linguagem Python

Zen of Python >>> import this

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass

class CalculadoraCientifica:
    pass


[2] - Utilize nomes minúsculo separados em underline para funções ou variáveis;

def soma():
    pass

def soma_dois():
    pass

[3] - Utilize 4 espaços para identação;

if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco;

[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;

# Import errado
- import sys, os

# Import correto
- import sys
- import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo de arquivo, logo depois de quaisquer comentários ou docstrings e antes de
constantes ou variáveis globais.

[6] - Espaços em expressões e instruções

# Não faça:

1- funcao( algo[ 1 ], { outro: 2 } )
2- algo (1)
3- dict ['chave'] = lista [indice]
4- x              = 1
5- y              = 2
6- variavel_longa = 3

# Faça
1- funcao(algo[1], {outro: 2})
2- algo(1)
3- dict['chave'] = lista[indice]
4- x = 1
5- y = 2
6- variavel_longa = 3


[7] - Termine sempre uma instrução com uma nova linha.
"""
