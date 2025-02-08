
# Funções - Revisão


# Definição da função
def soma_total(a, b, c, d=0):
    # Os valores dentro dos parenteses são chamados de parametros e são utilizados para dar dinamismo a função, eles podem assumir qualquer valor que informarmos pra eles NA EXECUÇÃO da função, ou seja quando ela é "chamada"

    return a + b + c + d


nomes = ["Ana", "Carlos", "Fernanda", "Gabriel", "Juliana", "Lucas", "Mariana", "Pedro", "Roberta", "Tiago"]

sobrenomes = ["Silva", "Souza", "Oliveira", "Costa", "Pereira", "Lima", "Gomes", "Martins", "Alves", "Rodrigues"]


def nomeCompleto(n, s):
    return f'{n} {s}'

listaCompleta = []
i = 0
for nome in nomes:
    completo = nomeCompleto(nome, sobrenomes[i])
    i += 1
    listaCompleta.append(completo)

print(listaCompleta)