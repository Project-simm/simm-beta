# Nome do usuario que está logado no site. Neste caso vamo de admin mesmo
uname = "ADMIN"
# Senha do usuário (eu usava essa senha com 8 anos, não me julgue)
pwd = "@Tigresas279"
# Pasta em que estão todas as configurações da wallet
cdir = "C:/Totonho/Site-flask/config_dir/"
# Local em sí da wallet. A wallet é um arquivo que armazena muitas coisas, mas principalmente chaves e certificados. 
# Isso provavelmente vai dar um problema de segurança futuramente, então é uma boa modificar.
wltloc = "C:/Totonho/Site-flask/config_dir/"
# Senha da wallet
wltpwd = "@Tigresas279"
# É uma estrutura de dados usada para descrever uma conexão a uma fonte de dados. Basicamente um link pro banco de dados.
dsn = "(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.us-ashburn-1.oraclecloud.com))(connect_data=(service_name=g7d8724ca4c835e_nomeloucoparadatabase_medium.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"