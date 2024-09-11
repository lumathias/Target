""" 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua 
preferência ou pode ser previamente definida no código. """

def conta_a(texto):
  cont = 0
  found = False

  for caractere in texto:
    if caractere.lower() == 'a':
      cont += 1
      found = True
  if found:
    print(f"A letra 'a' foi found {cont} vezes na string.")
  else:
    print("A letra 'a' não foi found na string.")

# userinput = "Aprender programação pode ser divertido."
userinput = input("Digite uma frase: ")
conta_a(userinput)