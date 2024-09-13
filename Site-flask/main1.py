from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import logging
import oracledb
from walletcredentials import uname, pwd, dsn, cdir, wltloc, wltpwd

app = Flask(__name__, static_folder="static")
app.secret_key = "your_secret_key"  # Importante para a sessão

# Configurando o logging corretamente
logging.basicConfig(level=logging.INFO)

# Função para conexão ao banco e execução de SQL
def execute_sql(sql, params=None, fetch=False):
    try:
        with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, params or {})
                if fetch:
                    return cursor.fetchone()
                connection.commit()
    except Exception as e:
        logging.error(f"Erro ao executar SQL: {e}")
        raise

# Rota para renderizar a página de login/registro
@app.route("/")
def login():
    return render_template("index_login.html")

# Rota de registro de usuário
@app.route('/register', methods=['POST'])
def register():
    nome = request.form.get('nome')
    email = request.form.get('email')
    password = request.form.get('password')

    if not nome or not email or not password:
        return jsonify({"error": "Todos os campos são obrigatórios"}), 400

    try:
        sql = "INSERT INTO USUARIOS (USER_NOME, USER_EMAIL, USER_SENHA) VALUES (:nome, :email, :password)"
        execute_sql(sql, {"nome": nome, "email": email, "password": password})

        session['user_email'] = email
        return redirect(url_for('home'))
    except oracledb.IntegrityError:
        return jsonify({"error": "Email já registrado"}), 400
    except Exception as e:
        logging.error(f"Erro no registro do usuário: {e}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rota de login de usuário
@app.route('/login', methods=['POST'])
def handle_login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"error": "Email e senha são obrigatórios"}), 400

    try:
        query = "SELECT USER_SENHA FROM USUARIOS WHERE USER_EMAIL = :email"
        result = execute_sql(query, {"email": email}, fetch=True)

        if result and result[0] == password:
            session['user_email'] = email
            return redirect(url_for('home'))
        else:
            return jsonify({"error": "Credenciais inválidas"}), 401
    except Exception as e:
        logging.error(f"Erro no login: {e}")
        return jsonify({"error": "Erro interno do servidor"}), 500

# Rota para página do usuário
@app.route('/usuario')
def home():
    user_email = session.get('user_email')
    if not user_email:
        return redirect(url_for('login'))

    query = "SELECT USER_NOME FROM USUARIOS WHERE USER_EMAIL = :email"
    result = execute_sql(query, {"email": user_email}, fetch=True)

    user_name = result[0] if result else 'Usuário não encontrado'
    return render_template('index.html', user_name=user_name)

# Rota para exibir o template de cadastro de remédios
@app.route('/cadastro', methods=['GET'])
def exibir_cadastro():
    return render_template('gerenciador.html')

# Rota para cadastrar remédios
@app.route('/cadastro', methods=['POST'])
def cadastrar_remedio():
    if 'user_email' not in session:
        return jsonify({"error": "Usuário não autenticado"}), 401

    user_email = session['user_email']

    # Obter o user_id com base no email do usuário logado
    query = "SELECT USER_ID FROM USUARIOS WHERE USER_EMAIL = :email"
    user = execute_sql(query, {'email': user_email}, fetch=True)

    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 400

    user_id = user[0]  # user_id é retornado da consulta

    # Dados do remédio a partir da requisição
    data = request.json
    nome = data.get('nome')
    data_remedio = data.get('date')
    hora = data.get('time')
    repeticao = data.get('time_repeat')

    sql = """
        INSERT INTO REMEDIOS (REMEDIO_NOME, REMEDIO_DATA, REMEDIO_HORA, REMEDIO_REPETICAO, USER_ID)
        VALUES (:nome, TO_DATE(:data_remedio, 'YYYY-MM-DD'), :hora, :repeticao, :user_id)
    """
    try:
        execute_sql(sql, {'nome': nome, 'data_remedio': data_remedio, 'hora': hora, 'repeticao': repeticao, 'user_id': user_id})
        return jsonify({"message": "Remédio cadastrado com sucesso!"}), 200
    except Exception as e:
        logging.error(f"Erro ao cadastrar remédio: {e}")
        return jsonify({"error": "Erro ao cadastrar o remédio"}), 500

# Rota para editar remédios
@app.route("/edit/<int:remedio_id>", methods=['GET', 'POST'])
def editar_remedio(remedio_id):
    if request.method == 'POST':
        nome = request.form['nome']
        data = request.form['date']
        hora = request.form['time']
        repeticao = request.form['number']
        
        # Implementar atualização de remédio no banco
        sql = """
            UPDATE REMEDIOS
            SET REMEDIO_NOME = :nome, REMEDIO_DATA = TO_DATE(:data, 'YYYY-MM-DD'), REMEDIO_HORA = :hora, REMEDIO_REPETICAO = :repeticao
            WHERE REMEDIO_ID = :remedio_id
        """
        try:
            execute_sql(sql, {'nome': nome, 'data': data, 'hora': hora, 'repeticao': repeticao, 'remedio_id': remedio_id})
            return redirect(url_for('home'))
        except Exception as e:
            logging.error(f"Erro ao editar remédio: {e}")
            return jsonify({"error": "Erro ao editar o remédio"}), 500
    return render_template('gerenciador.html')

# Outras rotas
@app.route("/settings")
def config():
    return render_template("settings.html")

@app.route("/loading")
def loading():
    return render_template("loading.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
