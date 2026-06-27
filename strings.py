#exercicio 1

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

nomecompleto = nome + " " + sobrenome

print(f"Bem vindo/a, {nomecompleto}")

#exercicio 2

frase = input("Digite a frase: ")

espacos = frase.count(" ")

print("Espaços em branco:", espacos)

#exercicio 3

nome = input("Digite seu nome: ")

for i in range(1, len(nome) + 1):
  print(nome[:i])

#exercicio 4

numero = input("Digite o numero: ")

if len(numero) == 8:
  numero = "9" + numero
if len (numero) == 9:
  if numero[0]!= "9":
    numero = "9" + numero[1:]

print(f"Numero completo: {numero[:5]}-{numero[5:]}")
