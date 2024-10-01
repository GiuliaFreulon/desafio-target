'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

import math

def quadradoPerfeito(x):
    raiz = int(math.sqrt(x))
    return raiz * raiz == x

def fibonacci(numero):
    if numero < 0:
        print(f"O número {numero} não pertence à sequência de fibonacci")
        return
    
    resultado1 = 5 * numero * numero + 4
    resultado2 = 5 * numero * numero - 4

    if (quadradoPerfeito(resultado1) or quadradoPerfeito(resultado2)):
        print(f"O número {numero} pertence à sequência de fibonacci")
    else:
        print(f"O número {numero} não pertence à sequência de fibonacci")
