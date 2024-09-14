""" 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua 
preferência ou pode ser previamente definida no código. """

def conta_a(texto):
  cont = 0 # conta as vezes que 'a' aparece
  found = False # boleano para checar se 'a' aparece

  for caractere in texto: 
    if caractere.lower() == 'a': # checa se o char é 'a'
      cont += 1
      found = True
  if found:
    print(f"A letra 'a' foi encontrada {cont} vezes na string.")
  else:
    print("A letra 'a' não foi encontrada na string.")

# userinput = "Aprender programação pode ser bastante divertido."
userinput = input("Digite algo > ")
conta_a(userinput) 