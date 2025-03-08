#Exercício:

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

     
class Pessoa:
    def __init__(self, nome, sobrenome, matricula, endereco, cpf, data_de_nascimento, funcao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.matricula = matricula
        self.endereco = endereco
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.status = True
        self.funcao = funcao

class Biblioteca:
    def __init__(self, nome, endereco, horario):
        self.nome = nome
        self.endereco = endereco
        self.horario = horario
        self.catalogo = []
        self.usuarios = []
        self.funcionarios = []

    def cadastrar_usuarios(self, usuario: Pessoa):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)
    
    def cadastrar_livros(self, livro:Livro):
        self.catalogo.append(livro)
        print('Livro cadastrado com sucesso!')

    def emprestar_livro(self, livro):
        if not livro.emprestado and livro in self.catalogo:
            livro.emprestado = True
            print('Livro emprestado com sucesso!')
        else:
            print('Livro indisponível ou emprestado')

    def devolver_livro(self, livro):
        if livro.emprestado:
            livro.emprestado = False
            print('Livro devolvido com sucesso')



def menu():
    print('Escolha sua opção:')
    print('1 - Cadastrar usuário')
    print('2 - Cadastrar livro')
    print('3 - Emprestar livro')
    print('4 - Devolver livro')
    print('5 - Sair do sistema')

    opcao = input('Digite sua opcao: ')


