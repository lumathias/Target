""" 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua 
preferência ou pode ser previamente definida no código. """

def conta_a(string):
    cont = string.lower().count('a') # Convertemos a string para minúsculas para contar tanto 'a' quanto 'A' de uma vez
    
    if cont > 0:
        print(f"A letra 'a' aparece {cont} vezes na string.")
    else:
        print("A letra 'a' não foi encontrada na string.")

# String informada diretamente no código
# string_predefinida = "Aprender programação pode ser divertido."
# conta_a(string_predefinida)

userinput = input("Digite uma string: ")
conta_a(userinput)
