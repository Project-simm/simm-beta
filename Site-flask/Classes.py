import oracledb
from walletcredentials import uname, pwd, cdir, wltloc, wltpwd, dsn

class Usuario():
    def __init__(self, user, nome, sobrenome, senha, email):
        self.user = user
        self.nome = nome
        self.sobrenome = sobrenome
        self.senha = senha
        self.email = email
        self.user_id = 1
        self.table = 'jujuba'
        usuario = 'USER_APELIDO'
        usuario_nome = 'USER_NOME'
        usuario_sobrenome = 'USER_SOBRENOME'
        usuario_senha = 'USER_SENHA'
        usuario_email = 'USER_EMAIL'
        usuario_ID = 'USER_ID'

    def alterar_usuario(self):
        sql = f'''
            UPDATE USUARIOS
            SET USER_APELIDO = 'Yesnt'
            WHERE USER_ID = '{self.user_id}'
            '''
        with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
        
    def alterar_nome(self):
        sql = f'''
            UPDATE USUARIOS
            SET USER_NOME = 'Markus'
            WHERE USER_ID = '{self.user_id}'
            '''
        with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
        
    def alterar_sobrenome(self):
        sql = f'''
            UPDATE USUARIOS
            SET USER_SOBRENOME = 'Hiago'
            WHERE USER_ID = '{self.user_id}'
            '''
        with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
    
    def alterar_senha(self):
        sql = f'''
            UPDATE USUARIOS
            SET USER_SENHA = 'pirocopterosuicida'
            WHERE USER_ID = '{self.user_id}'
            '''
        with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
        
    def alterar_email(self):
        sql = f'''
            UPDATE USUARIOS
            SET USER_EMAIL = '2132312.com'
            WHERE USER_ID = '{self.user_id}'   
            '''
        with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()

    def criar_usuario(self):
        sql = f'''
            INSERT INTO USUARIOS (USER_APELIDO, USER_NOME, USER_SOBRENOME, USER_SENHA, USER_EMAIL)
            VALUES ('{self.user}', '{self.nome}', '{self.sobrenome}', '{self.senha}', '{self.email}')
            '''
        with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()

class Login():
    def __init__(self):
        self.email = ''
        self.senha = ''
    
    def verifica_existencia(self):
        sql = f'''
            UPDATE USUARIOS
            SET USER_SENHA = 'pirocopterosuicida'
            WHERE USER_ID = '{self.user_id}'
            '''
        with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()

def autenticar_usuario(email, senha):
    try:
        with oracledb.connect(user=uname, password=pwd, dsn=dsn, config_dir=cdir, wallet_location=wltloc, wallet_password=wltpwd) as connection:
            with connection.cursor() as cursor:
            # Query para buscar o usuário com o email e senha fornecidos
                cursor.execute("""
                    SELECT user_email 
                    FROM usuarios 
                    WHERE user_email = :email AND user_senha = :senha
                """, {"email": email, "senha": senha})
            
            # Verifica se algum resultado foi encontrado
                result = cursor.fetchone()
                if result:
                    print("Login bem-sucedido!")
                    return True
                else:
                    print("Email ou senha incorretos.")
                    return False

    except oracledb.DatabaseError as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return False
    
#email = input("Digite seu email: ")
#senha = input("Digite sua senha: ")

#if autenticar_usuario(email, senha):
    print("Acesso concedido!")
#else:
    print("Acesso negado!")
    
u1 = Usuario('MEIA','ARTHUR','HIAGO','12345','juliocezarcomunista@gmail.com')
u1.criar_usuario()