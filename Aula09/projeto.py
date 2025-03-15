#SISTEMA DE HAMBURGUERIA:

#"Estou querendo criar um sistema pra minha hamburgueria... 
# Vou precisar de um cardápio, um sistema de fidelização de clientes,
# e um jeito pra pessoa poder fazer pedido e vir aqui pegar ou mandar motoboy entregar?
# E aí você consegue fazer até semana que vem?"

class Cliente():
    def __init__(self,nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        
    def __str__(self):
        return f"Nome:{self.nome},Endereco:{self.endereco}, Telefone:{self.telefone}"   
    # Essa função define o objeto da classe
    
class Cardapio():
    def __init__(self):
        # Dicionário para armazenar as informações do cardápio
        self.itens = [
        {"tipo":"vegetariano","hamburger": "x-salada" ,"preco":"60"},
        {"tipo":"normal","hamburger": "x-tudo" ,"preco":"30"},
        {"tipo":"normal","hamburger": "x-bacon" ,"preco":"25"}
        ]
    def exibir_cardapio(self):
        # Função para exibir os itens do cardapio
        print("n\{Cardapio}")
        for item in self.itens:
            print(f"Tipo:{item['tipo']},Hamburger:{item['hamburger']} , Preco:R${item['preco']} ")
        print("\n")
                

class Hamburgueria():
    def __init__(self, cardapio:Cardapio, cliente: Cliente,):
        self.cardapio = cardapio
        self.clientes = cliente
        
    def mostrar_informacoes_clientes(self):
        print('Informações do cliente:')
        print(self.cliente)
        
    def  mostrar_cardapio(self):
        self.cardapio.mostrar_cardapio()  

#Criando um cliente     
nome =input("Nome:")        
endereco = input("Endereco:")
telefone = input("Telefone:")        
cliente =nome, endereco, telefone

#Criando a hamburgeria com o cliente e o cardapio
hamburgueria = Hamburgueria(Cliente,Cardapio)

# Mostrar as informações do cliente
hamburgueria.mostrar_informacoes_cliente()

# Mostrar o cardápio
hamburgueria.mostrar_cardapio()
