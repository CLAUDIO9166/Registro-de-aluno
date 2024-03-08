import sqlite3

#criando tabela
#cursor.execute(''' CREATE TABLE usuario (
#                    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                    nome TEXT NOT NULL,
#                    idade INT NOT NULL);''')

#cursor.execute(''' INSERT INTO usuario (nome, idade) VALUES('Jorge', 55) ''')

# Atualizando dados
with sqlite3.connect('usuario.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute(''' UPDATE usuario SET idade=17 WHERE id=1 ''')
    conexao.commit()

# Deletando dados
with sqlite3.connect('usuario.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute(''' DELETE FROM usuario WHERE idade < 18  ''')
    conexao.commit()

# Imprimindo os dados
with sqlite3.connect('usuario.db') as conexao:
    cursor = conexao.cursor()
    cursor.execute(''' SELECT * FROM usuario''')
    resultado = cursor.fetchall()

for linha in resultado:
    print(linha)