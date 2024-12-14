# Exercício 1: Escreva um programa que recebe dois números como entrada e imprime o maior deles.
numero1 =int(input("Digite um numero:"))
numero2 =int(input("Digite outro numero:"))
if numero1 > numero2:
   print("numero1")
elif numero1 < numero2:
   print("numero2")   
# Exercício 2: Crie um programa que recebe uma string e verifica se a primeira letra é vogal.
nome = input('Digite seu nome:')
if nome[0] in 'aeiou':
   print("é uma vogal")
else:
   print("Não é uma vogal")
# Exercício 3: Escreva um programa que solicita a idade do usuário e determina se ele é elegível para votar (18 anos ou mais).
idade = int(input("Digite sua Idade:"))
if idade >=18:
   print("Voce pode votar")
elif idade <18:
   print("Voce não pode votar")   
# Exercício 4: Crie um programa que recebe uma string como entrada e verifica se ela começa com a letra 'A'. Imprima "Começa com A" se for verdadeiro, caso contrário, imprima "Não começa com A".
nome = 'Digite seu nome'
if nome[0].lower() in 'a':
   print("Começa com A")
else:
   print("Não começa com a")

# Exercício 5: Escreva um programa que solicita ao usuário uma senha. Se a senha for "12345", imprima "Acesso concedido"; caso contrário, imprima "Acesso negado".
senha_valida =["12345"]
print(senha_valida[0])
n = 0
print(len(senha_valida))
senha_digitada = input("Digite sua senha")
if senha_digitada == senha_valida[n]:
   print("acesso concedido")
else:
   print("Acesso negado")


# Exercício 6: Crie um programa que determina se um ano dado é bissexto. Um ano bissexto é divisível por 4, mas não é divisível por 100, a menos que também seja divisível por 400.

# Exercício 7: Crie um programa que recebe como entrada a altura, profissão e nome de um individuo e: 
# Se o nome for Alice e a altura for 169, exiba a mensagem: "Suspeito encontrado"
# Se o nome for Douglas ou Rafael e a profissão começar com a letra C, exiba a mensagem: "Suspeito encontrado"
# Se o nome encontrado for Thiago e a profissão for 'Professor', exiba mensagem: Suspeito encontrado!