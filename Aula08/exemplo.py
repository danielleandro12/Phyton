#Exemplo propriedades compartilhadas fora do método __init__

class Pessoa:
    nomes_unicos = set()
    def __init__(self, nome):
        self.nome = nome
        self.nomes_unicos.add(nome)


pessoa1 = Pessoa('Thiago')

print(pessoa1.nome)

pessoa2 = Pessoa('Amanda')

pessoa3 = Pessoa('Thiago')


print(pessoa1.nomes_unicos)



#EXEMPLO:


class Livro:
    def __init__(self, titulo, autor, ano, categoria, editora, ISBN):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.categoria = categoria
        self.editora = editora
        self.ISBN = ISBN
        self.emprestado = False

    def __str__(self):
        return self.titulo

# Localidade do livro na biblioteca
class Estante:
    def __init__(self, numero, fileira, andar, categoria):
        self.numero = numero
        self.fileira = fileira
        self.andar = andar
        self.categoria = categoria
        self.livros = []
    
    def listar_livros_na_estante(self):
        lista = []
        for livro in self.livros:
            lista.append(livro)
        print(livro)

class Pessoa:
    def __init__(self, nome, sobrenome, matricula, endereco, cpf, data_de_nascimento=''):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.endereco = endereco
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.status = True
    
class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, matricula, endereco, cpf, funcao):
        super().__init__(nome, sobrenome, matricula, endereco, cpf)
        self.funcao = funcao
    
    def __str__(self):
        return self.nome
    
    def cadastrar_livros(self, livro:Livro, estante: Estante, biblioteca):
        estante.livros.append(livro)
        biblioteca.catalogo.append(livro)


class Biblioteca:
    def __init__(self, nome, endereco, horario):
        self.nome = nome
        self.endereco = endereco
        self.horario = horario
        self.catalogo = []
        self.usuarios = []
        self.funcionarios = []

    def cadastrar_funcionarios(self, funcionario: Funcionario):
        self.funcionarios.append(funcionario)
    
    def listar_funcionarios(self):
        for funcionario in self.funcionarios:
            print(funcionario)

    def cadastrar_usuarios(self, usuario: Pessoa):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)    
    

horario = {
    'Segunda': ('10:00', '17:00'),
    'Terça': ('10:00', '17:00'),
    'Quarta': ('10:00', '17:00'),
    'Quinta': ('10:00', '17:00'),
    'Sexta': ('10:00', '17:00'),
    'Sábado': ('10:00', '17:00'),
}

biblioteca = Biblioteca('Biblioteca Municipal de Belo Horizonte', 'Rua das Flores 176', horario)

funcionario = Funcionario('Bruno', 'Dias', '14A7B', 'Rua das Camélias 154', '076.106.123-32', 'Bibliotecário')

funcionario2 = Funcionario('Rodrigo', 'Silva', '24SB', 'Av X', '1233', 'Admin')

biblioteca.cadastrar_funcionarios(funcionario)

biblioteca.cadastrar_funcionarios(funcionario2)

biblioteca.listar_funcionarios()

livro = Livro('Boa vida', 'Zero', 1994, 'Terror', 'Boavida', '123SV')

estante = Estante(1, 'A', 2, 'Terror')

funcionario2.cadastrar_livros(livro, estante, biblioteca)

estante.listar_livros_na_estante()