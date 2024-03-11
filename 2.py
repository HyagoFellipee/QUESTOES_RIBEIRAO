
# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;


def fibonacci(n):
    a = 0
    b = 1 

    if n == 0 or n == 1:
        print(f'{n} pertence a sequência de Fibonacci')
        return

    while b < n:
        a, b = b, a+b

    if b == n:
        print(f'{n} pertence a sequência de Fibonacci')
    else:
        print(f'{n} não pertence a sequência de Fibonacci')


n = int(input('Digite um número: '))
fibonacci(n)

    