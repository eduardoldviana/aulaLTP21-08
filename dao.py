import sqlite3

DATABASE = "meu_banco.db"

def get_db_connection():
    conexao = sqlite3.connect(DATABASE)
    conexao.row_factory = sqlite3.Row
    return conexao

def listar_todos_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor()
    usuarios = cursor.execute('SELECT * FROM usuarios').fetchall()
    conn.close()
    return usuarios
def inserir_usuario(nome, email):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()
def deletar_usuario_por_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conn.commit()
    conn.close()


def create_user_table():
    conexao = get_db_connection()
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
    conexao.close()

def insert_user(nome, email):
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute(
        '''
            INSERT INTO usuarios(nome, email) VALUES (?, ?);
        '''
        , (nome, email)
    )
    cursor.commit()
    conexao.close()

def get_all_users():
    conexao = get_db_connection()
    cursor = conexao.cursor()
    cursor.execute(
        '''
            SELECT * FROM usuarios;
        '''
    )
    usuarios = cursor.fetchall()
    # Converte o formato ROW do sqlite3 para Dicionario
    usuarioDict = [dict(u) for u in usuarios]
    conexao.close()
    return usuarioDict

def update_user_email_by_id(email, id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
            UPDATE usuarios
            set email = ?
            WHERE id = ?;
        '''
        , (email, id)
    )
    conn.execute()
    conn.close()

def select_user_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
            SELECT * FROM usuarios WHERE id = ?;
        '''
        , (id, )
    )
    user = dict(cursor.fetchone())
    conn.close()
    return user
# 1. Conecta-se ou cria o arquivo do banco de dados
# conexao = sqlite3.connect('meu_banco.db')

# # 2. Cria um cursor para executar comandos SQL
# cursor = conexao.cursor()

# cursor.execute(
#     '''
#         CREATE TABLE IF NOT EXISTS usuarios(
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             nome TEXT NOT NULL,
#             email TEXT NOT NULL UNIQUE
#         )
#     '''
# )

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

# cursor.execute(
#     '''
#         SELECT * FROM usuarios WHERE id = ?;
#     '''
#     , (1, )
# )

# usuario = cursor.fetchall() # Retorna todos os resultados do SELECT anterior como lista no Python
# usuario = cursor.fetchone() # Retorna uma lista com os dados da linha
# print(f"Id: {usuario[0]} - Nome: {usuario[1]} - Email: {usuario[2]}")

# for u in usuario:
# #     print(f"Id: {u[0]} - Nome: {u[1]} - Email: {u[2]}")

# cursor.execute(
#     '''
#         UPDATE usuarios
#         SET email = ?
#         WHERE id = ?;
#     '''
#     , ("eldviana@gmail.com", 1)
# )

# cursor.execute(
#     '''
#         DELETE FROM usuarios
#         WHERE id = ?;
#     '''
#     , (2, )
# )

# conexao.commit() # Aplica o SQL ao banco
# conexao.close()

# print("Conexão com banco estabelecida.")