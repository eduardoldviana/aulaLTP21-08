import sqlite3

# 1. Conecta-se ou cria o arquivo do banco de dados
conexao = sqlite3.connect('meu_banco.db')

# 2. Cria um cursor para executar comandos SQL
cursor = conexao.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS usuarios(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    '''
)
conexao.commit() # Aplica o SQL ao banco
conexao.close()
