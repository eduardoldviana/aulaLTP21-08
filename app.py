from flask import Flask, render_template, jsonify, request
import sqlite3
from dao import get_all_users, select_user_by_id, inserir_usuario

app = Flask(__name__)

def get_db_connection():
    conexao = sqlite3.connect("meu_banco.db")
    conexao.row_factory = sqlite3.Row
    return conexao

# http://localhost:5000/usuarios
@app.route("/usuarios")
def listar_usuarios():
    usuarios = get_all_users() #Importado de DAO
    # Retornar o resultado
    return jsonify(usuarios)
# http://localhost:5000/usuarios/1
@app.route("/usuarios/<int:id>")
def recuperar_usuarios(id):
    usuario = select_user_by_id(id) #Importado de DAO
    # Retornar um unico usuario
    return jsonify(usuario)

@app.route("/usuarios", methods = ['POST'])
def inserir_usario():
    #Importar requests de Flask
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    # Importar insert_user de DAO
    usuario = inserir_usario(nome, email)
    return f"Dados recebidos!"



if __name__ == '__main__':
    app.run(debug=True)