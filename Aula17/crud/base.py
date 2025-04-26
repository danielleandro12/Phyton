# Conecta ao banco de dados
import sqlite3

conexao = sqlite3.connect('banco_de_dados.db')

# Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

# Cria a tabela usuarios se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome VARCHAR,
    email VARCHAR
);
''')

def cadastra_usuario(nome, email):
    # Inserir dados na tabela
    sql = "INSERT INTO usuarios (nome, email) VALUES (?, ?)"
    cursor.execute(sql, (nome, email))
    conexao.commit() 


cadastra_usuario('Daniel', 'danielleandromelo1@gmail.com')
cadastra_usuario('Alex', 'alexsilva.contato@gmail.com') 


print(f"Consultando todos os usuários na tabela usuarios")

# Usa uma query segura com parâmetros
sql = "SELECT * FROM usuarios"
cursor.execute(sql)
result = cursor.fetchall()

# Imprime os resultados
print(result)
for linha in result:
    print(f"ID:{linha[0]}, Nome:{linha[1]}, Email:{linha[2]}")      

# Atualiza dados na tabela
def atualiza_usuario(id,nome,email):
    sql = "UPDATE usuarios SET nome = ?, email = ? WHERE id = ?"
    cursor.execute(sql, (nome, email, id))
    conexao.commit()


# Exclui dados da tabela
def exclui_usuario(id):
    sql = "DELETE FROM usuarios WHERE id = ?"
    cursor.execute(sql, (id,))
    conexao.commit()


# Fecha a conexão com o banco de dados
conexao.close()

