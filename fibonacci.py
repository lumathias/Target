""" 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre
será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a 
sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua 
preferência ou pode ser previamente definido no código """

def is_fibonacci(num):
  a, b = 0, 1 
  while b < num: # enquanto o numero for menor que valor a ser verificado gera-se a sequencia 
    a, b = b, a + b # a=b e b=b+a
   
  if b == num: # testa se b é o numero
    return f"O número {num} pertence à sequência de Fibonacci."
  else:
    return f"O número {num} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número > "))
print(is_fibonacci(numero))