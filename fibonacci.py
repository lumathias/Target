""" 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre
será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
"""
def fibonacci(number): # sequencia até o num dado 
    fibonacci_sequence = [0, 1] # inicia a sequencia com os dois primeiros num
    while True:
        next_fib = fibonacci_sequence[-1] + fibonacci_sequence[-2] # next = soma dos dois anteriores 
        fibonacci_sequence.append(next_fib) # adciona next no fim 
        if next_fib >= number: # caso next maior que num sai 
            break
    return fibonacci_sequence # caso contrario chama a func novamente

def is_fibonacci(num):
    sequence = fibonacci(num)
    if num in sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Digite um número para verificar na sequência de Fibonacci: "))
resultado = is_fibonacci(numero)
print(resultado)