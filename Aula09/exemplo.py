#Parte 1:
class Animal():
    reino = [] # atributo compartilhado entre todas as instâncias da classe
    def __init__(self, cor, tamanho, especie, idade):
        self.cor = cor # Esse tipo de atributo, que tem parametro no método init, precisa ser declarado na instânciação da classe.
        self.tamanho = tamanho
        self.especie = especie
        self.idade = idade
        self.conjunto = [] # Específico com os outros atributos construtor;

    def mover(self):
        print(f'O {self.especie} está se movendo')

salmao = Animal('vermelho', 'pequeno', 'peixis du mar', 19)

salmao.reino.append('peixes')

print(salmao.reino) 
print(salmao.conjunto)

salmao.conjunto.append('Cardume') # A propriedade conjunto é exclusiva da INSTÂNCIa da classe, ou seja, não é compartilhada com outras instâncias. Dessa forma, salmão possui a string "Cardume" como um elemento dentro da lista de seu atributo conjunto, mas o cachorro não.


cachorro = Animal('caramelo', 'médio', 'vira-lata', 10)


print(cachorro.reino) # Como o atributo reino está na "raiz" da classe ele é compartilhdo por TODAS as instâncias da classe, então como foi atribuido uma informação à propriedade reino da instância "salmao" a instância cachorro também tem essa informação.
print(cachorro.conjunto)

cachorro.mover() # Métodos de classe permitem que elas executem determinados comportametos
salmao.mover()

class Animal():
    reino = [] # atributo compartilhado entre todas as instâncias da classe
    def __init__(self, cor, tamanho, especie, idade = None):
        self.cor = cor # Esse tipo de atributo, que tem parametro no método init, precisa ser declarado na instânciação da classe.
        self.tamanho = tamanho
        self.especie = especie
        self.idade = idade
        self.conjunto = [] # Específico com os outros atributos construtor;

    def mover(self):
        print(f'O {self.especie} está se movendo')

salmao = Animal('vermelho', 'pequeno', 'peixis du mar', 19)

salmao.reino.append('peixes')

print(salmao.reino) 
print(salmao.conjunto)

salmao.conjunto.append('Cardume') # A propriedade conjunto é exclusiva da INSTÂNCIa da classe, ou seja, não é compartilhada com outras instâncias. Dessa forma, salmão possui a string "Cardume" como um elemento dentro da lista de seu atributo conjunto, mas o cachorro não.


cachorro = Animal('caramelo', 'médio', 'vira-lata', 10)


print(cachorro.reino) # Como o atributo reino está na "raiz" da classe ele é compartilhdo por TODAS as instâncias da classe, então como foi atribuido uma informação à propriedade reino da instância "salmao" a instância cachorro também tem essa informação.
print(cachorro.conjunto)

cachorro.mover() # Métodos de classe permitem que elas executem determinados comportametos
salmao.mover()


# Parte 2;

class Gato(Animal):
    def __init__(self, cor, tamanho, especie, nome):
        super().__init__(cor, tamanho, especie)
        self.__nome = nome

    def mover(self): # É possível re-escrever métodos de classe para adapta-los mehor à nossa necessidade específica.
        print(f'O gato {self.__nome} se move com preguiça' )

meu_gato = Gato('laranja', 'pequeno', 'gatitu', 'Matusalem')
meu_gato.mover()

print(meu_gato.__nome)


class Pessoa():
    def __init__(self, nome):
        self.__nome: nome

        @property
        def nome(self):
            return self.__nome
        
pessoa = Pessoa('Alice')
