import logging
import sqlite3
import espelhodbtxt

import base64
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from conexao import criar_tabela, inserir_usuario, buscar_usuario, buscar_usuario_por_id, atualizar_usuario, excluir_usuario

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = buscar_usuario(email=email, senha=senha)
        if usuario:
            return redirect(url_for('conteudo'))
        else:
            return "Usuário não encontrado."
    return render_template('base/login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto.filename != '':
                foto_data = foto.read()
                foto_base64 = base64.b64encode(foto_data).decode('utf-8')
                inserir_usuario(nome, email, senha, foto_base64)
                return redirect(url_for('login'))
    return render_template('base/cadast_user.html')

@app.route('/conteudo')
def conteudo():
    usuarios = buscar_usuario()
    return render_template('base/conteudo.html', usuarios=usuarios)

@app.route('/editar/<int:usuario_id>', methods=['GET', 'POST'])
def editar(usuario_id):
    usuario = buscar_usuario_por_id(usuario_id)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        if 'foto' in request.files:
            foto = request.files['foto']
            if foto.filename != '':
                foto_data = foto.read()
                foto_base64 = base64.b64encode(foto_data).decode('utf-8')
                atualizar_usuario(usuario_id, nome, email, senha, foto_base64)
                return redirect(url_for('conteudo'))
    return render_template('base/editreg.html', usuario=usuario)

@app.route('/excluir/<int:usuario_id>', methods=['POST'])
def excluir(usuario_id):
    excluir_usuario(usuario_id)
    return redirect(url_for('conteudo'))

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
