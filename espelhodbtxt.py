from flask import Flask, request
import logging

app = Flask(__name__)

# Configuração do logger
logging.basicConfig(filename='database.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Função para adicionar um novo usuário ao banco de dados e ao arquivo de backup
def adicionar_usuario(nome, email, senha):
    # Lógica para adicionar usuário ao banco de dados
    logging.info(f'Novo usuário adicionado: Nome={nome}, Email={email}')

    # Adicionar ao arquivo de backup
    with open('backup.txt', 'a') as backup_file:
        backup_file.write(f'Novo usuário adicionado: Nome={nome}, Email={email}\n')

# Função para editar um usuário existente no banco de dados e no arquivo de backup
def editar_usuario(nome, email, nova_senha):
    # Lógica para editar usuário no banco de dados
    logging.info(f'Usuário editado: Nome={nome}, Novo Email={email}, Nova Senha={nova_senha}')

    # Atualizar o arquivo de backup
    with open('backup.txt', 'r') as backup_file:
        lines = backup_file.readlines()
    with open('backup.txt', 'w') as backup_file:
        for line in lines:
            if f'Email={email}' in line:
                line = f'Usuário editado: Nome={nome}, Novo Email={email}, Nova Senha={nova_senha}\n'
            backup_file.write(line)

# Função para excluir um usuário do banco de dados e do arquivo de backup
def excluir_usuario(email):
    # Lógica para excluir usuário do banco de dados
    logging.info(f'Usuário excluído: Email={email}')

    # Remover do arquivo de backup
    with open('backup.txt', 'r') as backup_file:
        lines = backup_file.readlines()
    with open('backup.txt', 'w') as backup_file:
        for line in lines:
            if f'Email={email}' not in line:
                backup_file.write(line)

# Rotas do Flask
@app.route('/adicionar_usuario', methods=['POST'])
def adicionar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    adicionar_usuario(nome, email, senha)
    return 'Usuário adicionado com sucesso!'

@app.route('/editar_usuario', methods=['POST'])
def editar():
    nome = request.form.get('nome')
    email = request.form.get('email')
    nova_senha = request.form.get('nova_senha')
    editar_usuario(nome, email, nova_senha)
    return 'Usuário editado com sucesso!'

@app.route('/excluir_usuario', methods=['POST'])
def excluir():
    email = request.form.get('email')
    excluir_usuario(email)
    return 'Usuário excluído com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
