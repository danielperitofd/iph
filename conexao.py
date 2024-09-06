import sqlite3
import logging

# Configuração do logger
logging.basicConfig(filename='database.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def criar_tabela():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        foto TEXT
    )
    ''')
    conn.commit()
    conn.close()

def inserir_usuario(nome, email, senha, foto=None):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email, senha, foto) VALUES (?, ?, ?, ?)', 
                   (nome, email, senha, foto))
    conn.commit()
    conn.close()
    logging.info(f'Novo usuário adicionado: Nome={nome}, Email={email}')

def buscar_usuario(email=None, senha=None):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    if email and senha:
        cursor.execute('SELECT * FROM usuarios WHERE email=? AND senha=?', (email, senha))
    elif email:
        cursor.execute('SELECT * FROM usuarios WHERE email=?', (email,))
    else:
        cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios

def buscar_usuario_por_id(usuario_id):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id=?', (usuario_id,))
    usuario = cursor.fetchone()
    conn.close()
    return usuario

def atualizar_usuario(usuario_id, nome, email, senha, foto=None):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE usuarios SET nome=?, email=?, senha=?, foto=? WHERE id=?', 
                   (nome, email, senha, foto, usuario_id))
    conn.commit()
    conn.close()
    logging.info(f'Usuário atualizado: ID={usuario_id}, Nome={nome}, Email={email}')

def excluir_usuario(usuario_id):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=?', (usuario_id,))
    conn.commit()
    conn.close()
    logging.info(f'Usuário excluído: ID={usuario_id}')
