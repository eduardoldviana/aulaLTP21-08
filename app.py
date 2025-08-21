from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conexao = sqlite3.connect("meu_banco.db")
    conexao.row_factory = sqlite3.Row
    return conexao

# http://localhost:5000/usuarios
@app.route("/usuarios")
def listar_usuarios():
    # Recuperar a conoexão do 
    conexao = get_db_connection()
    # Recuperar a resposta do SELECT
    cursor = conexao.cursor()
    cursor.execute(
        '''
            SELECT * FROM usuarios;
        '''
    )
    usuarios = cursor.fetchall()
    # Converte formato ROW do sqlite3 para Dicionario
    usuario = [dict(u) for u in usuarios]


    # Fechar a conexão
    conexao.close()
    # Retornar o resultado
    return jsonify(usuario)

if __name__ == '__main__':
    app.run(debug=True)