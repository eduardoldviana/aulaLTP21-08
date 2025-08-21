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

# cursor.execute(
#     '''
#         INSERT INTO usuarios(nome, email) VALUES (?,?);
#     '''
#     , ("Eduardo Lopes Dornas Viana", "e.dornas@aluno.ifsp.edu.br")
# )

# cursor.execute(
#     '''
#         INSERT INTO usuarios(nome, email) VALUES (?,?);
#     '''
#     , ("Leonardo Lopes Dornas Viana", "leonardoldviana@gmail.com")
# )

cursor.execute(
    '''
        SELECT * FROM usuarios WHERE id = ?;
    '''
    , (1, )
)

# usuario = cursor.fetchall() # Retorna todos os resultados do SELECT anterior como lista no Python
usuario = cursor.fetchone() # Retorna uma lista com os dados da linha
print(f"Id: {usuario[0]} - Nome: {usuario[1]} - Email: {usuario[2]}")

# for u in usuario:
#     print(f"Id: {u[0]} - Nome: {u[1]} - Email: {u[2]}")

cursor.execute(
    '''
        UPDATE usuarios
        SET email = ?
        WHERE id = ?;
    '''
    , ("eldviana@gmail.com", 1)
)

cursor.execute(
    '''
        DELETE FROM usuarios
        WHERE id = ?;
    '''
    , (2, )
)

conexao.commit() # Aplica o SQL ao banco
conexao.close()

print("Conexão com banco estabelecida.")